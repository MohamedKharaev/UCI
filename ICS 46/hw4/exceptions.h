class ContainerOverflow : public exception
{
	const char * message;

public:
	ContainerOverflow(const char * err) : message(err) {}

	const char * what () const throw()
	{
		return message;
	}
};

class ContainerUnderflow : public exception
{
	const char * message;

public:
	ContainerUnderflow(const char * err) : message(err) {}

	const char * what () const throw()
	{
		return message;
	}
};
