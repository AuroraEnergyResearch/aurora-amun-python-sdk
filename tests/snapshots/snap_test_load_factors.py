# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_v1_and_v2_calculations result_v1'] = {
    'appliedParams': {
        'smoothingCoefficient': 0
    },
    'parameters': {
        'hubHeight': 90,
        'latitude': -22.71539,
        'loadFactorRequestId': 'SNAPSHOT',
        'longitude': 151.303711,
        'lossesAvailability': 0.1,
        'lossesElectrical': 0,
        'lossesEnvironmental': 0,
        'lossesOtherCurtailment': 0,
        'lossesTurbinePerformance': 0,
        'lossesWake': 0,
        'numberOfTurbines': 12,
        'obstacleHeight': 0,
        'p50GrossProduction': 0.4,
        'regionCode': 'aus_qld',
        'roughnessLength': 0.02,
        'smoothingCoefficient': None,
        'startTimeUTC': '2018-01-01T00:00:00.000Z',
        'turbineModelId': 268,
        'usePowerCurveSmoothing': False,
        'useReanalysisCorrection': False,
        'windType': 'P50Scaling'
    },
    'typical summary': {
        'count': 8760,
        'first day': [
            {
                'dateTime': '2018-01-01T00:00Z',
                'loadFactor': 0.4198,
                'windSpeed': 7.752088
            },
            {
                'dateTime': '2018-01-01T01:00Z',
                'loadFactor': 0.3451,
                'windSpeed': 7.262525
            },
            {
                'dateTime': '2018-01-01T02:00Z',
                'loadFactor': 0.3227,
                'windSpeed': 7.115541
            },
            {
                'dateTime': '2018-01-01T03:00Z',
                'loadFactor': 0.3639,
                'windSpeed': 7.385483
            },
            {
                'dateTime': '2018-01-01T04:00Z',
                'loadFactor': 0.4272,
                'windSpeed': 7.800093
            },
            {
                'dateTime': '2018-01-01T05:00Z',
                'loadFactor': 0.4978,
                'windSpeed': 8.229988
            },
            {
                'dateTime': '2018-01-01T06:00Z',
                'loadFactor': 0.5634,
                'windSpeed': 8.605756
            },
            {
                'dateTime': '2018-01-01T07:00Z',
                'loadFactor': 0.6025,
                'windSpeed': 8.829688
            },
            {
                'dateTime': '2018-01-01T08:00Z',
                'loadFactor': 0.6434,
                'windSpeed': 9.078203
            },
            {
                'dateTime': '2018-01-01T09:00Z',
                'loadFactor': 0.6898,
                'windSpeed': 9.404565
            },
            {
                'dateTime': '2018-01-01T10:00Z',
                'loadFactor': 0.7134,
                'windSpeed': 9.570967
            },
            {
                'dateTime': '2018-01-01T11:00Z',
                'loadFactor': 0.7807,
                'windSpeed': 10.064927
            },
            {
                'dateTime': '2018-01-01T12:00Z',
                'loadFactor': 0.8154,
                'windSpeed': 10.428367
            },
            {
                'dateTime': '2018-01-01T13:00Z',
                'loadFactor': 0.7354,
                'windSpeed': 9.725467
            },
            {
                'dateTime': '2018-01-01T14:00Z',
                'loadFactor': 0.626,
                'windSpeed': 8.964397
            },
            {
                'dateTime': '2018-01-01T15:00Z',
                'loadFactor': 0.5856,
                'windSpeed': 8.732835
            },
            {
                'dateTime': '2018-01-01T16:00Z',
                'loadFactor': 0.4518,
                'windSpeed': 7.961966
            },
            {
                'dateTime': '2018-01-01T17:00Z',
                'loadFactor': 0.3743,
                'windSpeed': 7.453397
            },
            {
                'dateTime': '2018-01-01T18:00Z',
                'loadFactor': 0.4745,
                'windSpeed': 8.09661
            },
            {
                'dateTime': '2018-01-01T19:00Z',
                'loadFactor': 0.6498,
                'windSpeed': 9.123451
            },
            {
                'dateTime': '2018-01-01T20:00Z',
                'loadFactor': 0.7761,
                'windSpeed': 10.017698
            },
            {
                'dateTime': '2018-01-01T21:00Z',
                'loadFactor': 0.8102,
                'windSpeed': 10.373949
            },
            {
                'dateTime': '2018-01-01T22:00Z',
                'loadFactor': 0.8094,
                'windSpeed': 10.365416
            },
            {
                'dateTime': '2018-01-01T23:00Z',
                'loadFactor': 0.7943,
                'windSpeed': 10.207993
            }
        ],
        'last day': [
            {
                'dateTime': '2018-12-31T00:00Z',
                'loadFactor': 0.487,
                'windSpeed': 8.168353
            },
            {
                'dateTime': '2018-12-31T01:00Z',
                'loadFactor': 0.4138,
                'windSpeed': 7.712389
            },
            {
                'dateTime': '2018-12-31T02:00Z',
                'loadFactor': 0.3585,
                'windSpeed': 7.350093
            },
            {
                'dateTime': '2018-12-31T03:00Z',
                'loadFactor': 0.3206,
                'windSpeed': 7.101582
            },
            {
                'dateTime': '2018-12-31T04:00Z',
                'loadFactor': 0.3418,
                'windSpeed': 7.240429
            },
            {
                'dateTime': '2018-12-31T05:00Z',
                'loadFactor': 0.3788,
                'windSpeed': 7.483197
            },
            {
                'dateTime': '2018-12-31T06:00Z',
                'loadFactor': 0.4129,
                'windSpeed': 7.706619
            },
            {
                'dateTime': '2018-12-31T07:00Z',
                'loadFactor': 0.4457,
                'windSpeed': 7.921661
            },
            {
                'dateTime': '2018-12-31T08:00Z',
                'loadFactor': 0.4819,
                'windSpeed': 8.138727
            },
            {
                'dateTime': '2018-12-31T09:00Z',
                'loadFactor': 0.5122,
                'windSpeed': 8.312363
            },
            {
                'dateTime': '2018-12-31T10:00Z',
                'loadFactor': 0.5179,
                'windSpeed': 8.345258
            },
            {
                'dateTime': '2018-12-31T11:00Z',
                'loadFactor': 0.5088,
                'windSpeed': 8.293209
            },
            {
                'dateTime': '2018-12-31T12:00Z',
                'loadFactor': 0.4737,
                'windSpeed': 8.091771
            },
            {
                'dateTime': '2018-12-31T13:00Z',
                'loadFactor': 0.4344,
                'windSpeed': 7.847798
            },
            {
                'dateTime': '2018-12-31T14:00Z',
                'loadFactor': 0.4155,
                'windSpeed': 7.723889
            },
            {
                'dateTime': '2018-12-31T15:00Z',
                'loadFactor': 0.4007,
                'windSpeed': 7.626421
            },
            {
                'dateTime': '2018-12-31T16:00Z',
                'loadFactor': 0.3968,
                'windSpeed': 7.601094
            },
            {
                'dateTime': '2018-12-31T17:00Z',
                'loadFactor': 0.4226,
                'windSpeed': 7.770546
            },
            {
                'dateTime': '2018-12-31T18:00Z',
                'loadFactor': 0.4654,
                'windSpeed': 8.044188
            },
            {
                'dateTime': '2018-12-31T19:00Z',
                'loadFactor': 0.5183,
                'windSpeed': 8.347334
            },
            {
                'dateTime': '2018-12-31T20:00Z',
                'loadFactor': 0.5352,
                'windSpeed': 8.444314
            },
            {
                'dateTime': '2018-12-31T21:00Z',
                'loadFactor': 0.498,
                'windSpeed': 8.231166
            },
            {
                'dateTime': '2018-12-31T22:00Z',
                'loadFactor': 0.4483,
                'windSpeed': 7.938896
            },
            {
                'dateTime': '2018-12-31T23:00Z',
                'loadFactor': 0.4092,
                'windSpeed': 7.682292
            }
        ],
        'load factor sum': 3153.6025,
        'wind speed sum': 61387.16359
    },
    'weatherYear summary': {
        'count': 8760,
        'first day': [
            {
                'dateTime': '2018-01-01T00:00Z',
                'loadFactor': 0.4388,
                'windSpeed': 7.876561
            },
            {
                'dateTime': '2018-01-01T01:00Z',
                'loadFactor': 0.3583,
                'windSpeed': 7.348971
            },
            {
                'dateTime': '2018-01-01T02:00Z',
                'loadFactor': 0.3342,
                'windSpeed': 7.190999
            },
            {
                'dateTime': '2018-01-01T03:00Z',
                'loadFactor': 0.3785,
                'windSpeed': 7.481275
            },
            {
                'dateTime': '2018-01-01T04:00Z',
                'loadFactor': 0.4467,
                'windSpeed': 7.928409
            },
            {
                'dateTime': '2018-01-01T05:00Z',
                'loadFactor': 0.5264,
                'windSpeed': 8.393606
            },
            {
                'dateTime': '2018-01-01T06:00Z',
                'loadFactor': 0.5976,
                'windSpeed': 8.801486
            },
            {
                'dateTime': '2018-01-01T07:00Z',
                'loadFactor': 0.6387,
                'windSpeed': 9.045089
            },
            {
                'dateTime': '2018-01-01T08:00Z',
                'loadFactor': 0.6772,
                'windSpeed': 9.31589
            },
            {
                'dateTime': '2018-01-01T09:00Z',
                'loadFactor': 0.7278,
                'windSpeed': 9.672225
            },
            {
                'dateTime': '2018-01-01T10:00Z',
                'loadFactor': 0.7537,
                'windSpeed': 9.85421
            },
            {
                'dateTime': '2018-01-01T11:00Z',
                'loadFactor': 0.8123,
                'windSpeed': 10.395587
            },
            {
                'dateTime': '2018-01-01T12:00Z',
                'loadFactor': 0.8505,
                'windSpeed': 10.794986
            },
            {
                'dateTime': '2018-01-01T13:00Z',
                'loadFactor': 0.7767,
                'windSpeed': 10.023356
            },
            {
                'dateTime': '2018-01-01T14:00Z',
                'loadFactor': 0.6595,
                'windSpeed': 9.19182
            },
            {
                'dateTime': '2018-01-01T15:00Z',
                'loadFactor': 0.6217,
                'windSpeed': 8.93968
            },
            {
                'dateTime': '2018-01-01T16:00Z',
                'loadFactor': 0.4757,
                'windSpeed': 8.103391
            },
            {
                'dateTime': '2018-01-01T17:00Z',
                'loadFactor': 0.3897,
                'windSpeed': 7.554412
            },
            {
                'dateTime': '2018-01-01T18:00Z',
                'loadFactor': 0.5011,
                'windSpeed': 8.249108
            },
            {
                'dateTime': '2018-01-01T19:00Z',
                'loadFactor': 0.6842,
                'windSpeed': 9.365246
            },
            {
                'dateTime': '2018-01-01T20:00Z',
                'loadFactor': 0.8073,
                'windSpeed': 10.343751
            },
            {
                'dateTime': '2018-01-01T21:00Z',
                'loadFactor': 0.8447,
                'windSpeed': 10.735127
            },
            {
                'dateTime': '2018-01-01T22:00Z',
                'loadFactor': 0.8438,
                'windSpeed': 10.725743
            },
            {
                'dateTime': '2018-01-01T23:00Z',
                'loadFactor': 0.8273,
                'windSpeed': 10.552701
            }
        ],
        'last day': [
            {
                'dateTime': '2018-12-31T00:00Z',
                'loadFactor': 0.5147,
                'windSpeed': 8.326814
            },
            {
                'dateTime': '2018-12-31T01:00Z',
                'loadFactor': 0.4323,
                'windSpeed': 7.833698
            },
            {
                'dateTime': '2018-12-31T02:00Z',
                'loadFactor': 0.3727,
                'windSpeed': 7.443181
            },
            {
                'dateTime': '2018-12-31T03:00Z',
                'loadFactor': 0.3319,
                'windSpeed': 7.176007
            },
            {
                'dateTime': '2018-12-31T04:00Z',
                'loadFactor': 0.3547,
                'windSpeed': 7.32521
            },
            {
                'dateTime': '2018-12-31T05:00Z',
                'loadFactor': 0.3946,
                'windSpeed': 7.586516
            },
            {
                'dateTime': '2018-12-31T06:00Z',
                'loadFactor': 0.4313,
                'windSpeed': 7.82747
            },
            {
                'dateTime': '2018-12-31T07:00Z',
                'loadFactor': 0.4681,
                'windSpeed': 8.0598
            },
            {
                'dateTime': '2018-12-31T08:00Z',
                'loadFactor': 0.5091,
                'windSpeed': 8.294721
            },
            {
                'dateTime': '2018-12-31T09:00Z',
                'loadFactor': 0.542,
                'windSpeed': 8.482922
            },
            {
                'dateTime': '2018-12-31T10:00Z',
                'loadFactor': 0.5482,
                'windSpeed': 8.518605
            },
            {
                'dateTime': '2018-12-31T11:00Z',
                'loadFactor': 0.5383,
                'windSpeed': 8.462149
            },
            {
                'dateTime': '2018-12-31T12:00Z',
                'loadFactor': 0.5002,
                'windSpeed': 8.243869
            },
            {
                'dateTime': '2018-12-31T13:00Z',
                'loadFactor': 0.4546,
                'windSpeed': 7.979954
            },
            {
                'dateTime': '2018-12-31T14:00Z',
                'loadFactor': 0.4342,
                'windSpeed': 7.846113
            },
            {
                'dateTime': '2018-12-31T15:00Z',
                'loadFactor': 0.4181,
                'windSpeed': 7.740928
            },
            {
                'dateTime': '2018-12-31T16:00Z',
                'loadFactor': 0.414,
                'windSpeed': 7.713608
            },
            {
                'dateTime': '2018-12-31T17:00Z',
                'loadFactor': 0.4419,
                'windSpeed': 7.896494
            },
            {
                'dateTime': '2018-12-31T18:00Z',
                'loadFactor': 0.4912,
                'windSpeed': 8.192357
            },
            {
                'dateTime': '2018-12-31T19:00Z',
                'loadFactor': 0.5486,
                'windSpeed': 8.520857
            },
            {
                'dateTime': '2018-12-31T20:00Z',
                'loadFactor': 0.567,
                'windSpeed': 8.626108
            },
            {
                'dateTime': '2018-12-31T21:00Z',
                'loadFactor': 0.5266,
                'windSpeed': 8.394883
            },
            {
                'dateTime': '2018-12-31T22:00Z',
                'loadFactor': 0.4713,
                'windSpeed': 8.078439
            },
            {
                'dateTime': '2018-12-31T23:00Z',
                'loadFactor': 0.4273,
                'windSpeed': 7.801212
            }
        ],
        'load factor sum': 3235.4522,
        'wind speed sum': 62368.276611
    }
}
