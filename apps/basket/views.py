from oscar.apps.basket.middleware import BasketMiddleware as CoreBasketMiddleware

class BasketMiddleware(CoreBasketMiddleware):
	
	def get_basket(self, request):
		"""
		Return the open basket for this request
		"""
		if request._basket_cache is not None:
			return request._basket_cache

		num_baskets_merged = 0
		manager = Basket.open
		cookie_key = self.get_cookie_key(request)
		cookie_basket = self.get_cookie_basket(cookie_key, request, manager)

		if hasattr(request, 'user') and user_is_authenticated(request.user):
			# Signed-in user: if they have a cookie basket too, it means
			# that they have just signed in and we need to merge their cookie
			# basket into their user basket, then delete the cookie.
			try:
				basket, __ = manager.get_or_create(owner=request.user)
			except Basket.MultipleObjectsReturned:
				# Not sure quite how we end up here with multiple baskets.
				# We merge them and create a fresh one
				old_baskets = list(manager.filter(owner=request.user))
				basket = old_baskets[0]
				for other_basket in old_baskets[1:]:
					self.merge_baskets(basket, other_basket)
					num_baskets_merged += 1

			# Assign user onto basket to prevent further SQL queries when
			# basket.owner is accessed.
			basket.owner = request.user

			if cookie_basket:
				self.merge_baskets(basket, cookie_basket)
				num_baskets_merged += 1
				request.cookies_to_delete.append(cookie_key)

		elif cookie_basket:
			# Anonymous user with a basket tied to the cookie
			basket = cookie_basket
		else:
			# Anonymous user with no basket - instantiate a new basket
			# instance.  No need to save yet.
			basket = Basket()

		# Cache basket instance for the during of this request
		request._basket_cache = basket
		return basket