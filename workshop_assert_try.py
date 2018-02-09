def mean(num_list):
	try:
		return sum(num_list)/len(num_list)
	except ZeroDivisionError as detail:
		msg= "\nCannot compute the mean value of an empty list."
		raise ZeroDivisionError(detail.__str__()+msg)
	except TypeError as detail :
		msg = "\nPlease pass a list of numbers not stings"
		raise TypeError(detail.__str__()+msg)
