Predictive Services Query Client (psquery)
==========================================

This package allows you to query Turi Predictive Services.

Refer to
https://turi.com/products/predictive-services/docs/userguide/connecting.html#psquery
for detailed information regarding how to use this client.

This package only includes the `config.py
<https://turi.com/products/predictive-services/docs/api/psclient/psclient.config.html>`_
and `query_client.py
<https://turi.com/products/predictive-services/docs/api/psclient/psclient.query_client.html>`_
from the full Predictive Services client psclient.


Connecting
----------

In order to connect, you need to know the query endpoint URL and your key. An
API key or an admin key is sufficient to query the Predictive Services. An API
key may have limitations on which endpoints it can query. Consult with your
system administrator to obtain the appropriate key.

The `psquery.connect
<https://turi.com/products/predictive-services/docs/api/psclient/psclient.query_client.html#psclient.query_client.connect>`_
function is used to connect to the service.::

    import psquery
    conn = psquery.connect(query_endpoint_URL, key_id)


Please consult the `connect function documentation
<https://turi.com/products/predictive-services/docs/api/psclient/psclient.query_client.html#psclient.query_client.connect>`_
for details on alternative methods of specifying these parameters during connection.


Querying
--------

Once you have connected, you can query by specifying the endpoint you want to
query and the parameters. Keep in mind that your key must have sufficient
privileges to access the endpoint. Admin keys can access all endpoints, but
API keys must be specifically allowed by endpoint name.::

    response = conn.query('add', 1, 2)

The response is a dict with the following keys and values.::

    {u'node': u'...', u'uuid': u'...', u'version': 1, u'from_cache': False, u'model': u'add', u'response': 3}

Please see the `query method documentation
<https://turi.com/products/predictive-services/docs/api/psclient/psclient.query_client.html#psclient.query_client.QueryClient.query>`_
for more details.

Feedback
--------

If the endpoint allows it, you can specify `feedback
<https://turi.com/products/predictive-services/docs/userguide/logging-feedback.html?highlight=feedback>`_:::

    conn.feedback(response['uuid'], success=True)

Please see the `feedback method documentation
<https://turi.com/products/predictive-services/docs/api/psclient/psclient.query_client.html#psclient.query_client.QueryClient.feedback>`_
for more details.



