from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    if 'here' in request.session:
        here = True
        request.session['here_count'] += 1
    else:
        here = False
        request.session['here'] = True
        request.session['here_count'] = 0

    return {'project': 'pyramid_test_app', 'here': here, 'here_count': request.session['here_count']}
