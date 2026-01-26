import dash

def incorporate_into_server_Dash(in_server_object):
    dash_app = dash.Dash(
        __name__,
        server = in_server_object,
        url_base_pathname = '/dashSection/'
    )
    return dash_app