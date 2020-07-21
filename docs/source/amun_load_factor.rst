Calculating Load Factors
====================================



.. automethod:: aurora.amun.client.session.AmunSession.run_load_factor_for_parameters
   :noindex: 


.. code-block::

     from aurora.amun.client.session import AmunSession 
     session  = AmunSession()

     base_parameters = LoadFactorBaseParameters(
        turbineModelId=6,
        latitude=59.59,
        longitude=0,
        startTimeUTC="2018-01-01T00:00:00.00Z",
        regionCode="GBR",
        hubHeight=90,
        obstacleHeight=0,
        wakeLoss=0.1,
        numberOfTurbines=12,
        roughnessLength=0.02,
        usePowerCurveSmoothing=False,
      )

      flow_parameters = WeibullParameters(measurementHeight=90, weibullScale=12, weibullShape=6)

      load_factors = session.run_load_factor_for_parameters(
        flow_parameters, base_parameters
      )

Common Parameters
====================================

.. autoclass:: aurora.amun.client.parameters.LoadFactorBaseParameters
   :members:
   :noindex: 

Flow Based Parameters
====================================

.. autoclass:: aurora.amun.client.parameters.BuiltInWindParameters
   :members:
   :noindex: 


.. autoclass:: aurora.amun.client.parameters.WeibullParameters
   :members:
   :noindex: 


.. autoclass:: aurora.amun.client.parameters.AverageWindSpeedParameters
   :members:
   :noindex: 



.. autoclass:: aurora.amun.client.parameters.PowerDensityParameters
   :members:
   :noindex: 
   