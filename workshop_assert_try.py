def mean(num_list):
	try:
	#	mean = sum(num_list)/len(num_list)
	# fail on different version tests
		mean = sum(num_list)/float(len(num_list))
	# fix the 2.7 version fail 		
		if isinstance(mean, complex):
			return NotImplemented
		return mean
	except ZeroDivisionError as detail:
		msg= "\nCannot compute the mean value of an empty list."
		raise ZeroDivisionError(detail.__str__()+msg)
	except TypeError as detail :
		msg = "\nPlease pass a list of numbers not stings"
		raise TypeError(detail.__str__()+msg)
