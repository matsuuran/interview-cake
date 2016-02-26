def get_products_of_all_ints_except_at_index(array):
	product_before_array = [1] * len(array)
	product_after_array  = [1] * len(array)
	product_before = 1
	product_after = 1

	for index, current_number in enumerate(array):
		product_before_array[index] = product_before
		product_before = product_before * current_number

		product_after_array[len(array)-index-1] = product_after
		product_after = product_after * array[len(array)-index-1]

	return [a*b for a,b in zip(product_before_array, product_after_array)]



