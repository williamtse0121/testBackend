from django.http import HttpResponse

def hello(request,offset):
	# assert False
	# try:
 #        offset = int(offset)
 #    except ValueError:
 #        raise Http404()

 #    assert False

	html = "<html><body>In %s hour(s), it will be.</body></html>" % (offset)
    	return HttpResponse(html)
