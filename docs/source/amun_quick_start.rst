Quick Start
====================================

.. code-block:: bash

      pip install git+https://github.com/AuroraEnergyResearch/aurora-amun-python-sdk

Add your Aurora Amun API key to the file *$home/*.aurora-api-key then import AmunSession and query the API.

.. code-block::

     from aurora.amun.client.session import AmunSession 
     session  = AmunSession()
     result  = session.get_scenarios("gbr")
     print(res[0])


Creating a Session
------------------------------
The :class:`AmunSession` handles credentials and connecting to the Amun API.

.. autoclass:: aurora.amun.client.session.AmunSession
   :noindex:


