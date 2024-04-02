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
        'windType': 'P50Scaling'
    },
    'typical summary': {
        'first day': [
            {
                'dateTime': '2018-01-01T00:00Z',
                'loadFactor': 0.4198,
                'windSpeed': 7.75208788280992
            },
            {
                'dateTime': '2018-01-01T01:00Z',
                'loadFactor': 0.3451,
                'windSpeed': 7.262525424330946
            },
            {
                'dateTime': '2018-01-01T02:00Z',
                'loadFactor': 0.3227,
                'windSpeed': 7.115541020157376
            },
            {
                'dateTime': '2018-01-01T03:00Z',
                'loadFactor': 0.3639,
                'windSpeed': 7.3854828354538435
            },
            {
                'dateTime': '2018-01-01T04:00Z',
                'loadFactor': 0.4272,
                'windSpeed': 7.800092832028858
            },
            {
                'dateTime': '2018-01-01T05:00Z',
                'loadFactor': 0.4978,
                'windSpeed': 8.229987827238713
            },
            {
                'dateTime': '2018-01-01T06:00Z',
                'loadFactor': 0.5634,
                'windSpeed': 8.605756373155907
            },
            {
                'dateTime': '2018-01-01T07:00Z',
                'loadFactor': 0.6025,
                'windSpeed': 8.829687751319256
            },
            {
                'dateTime': '2018-01-01T08:00Z',
                'loadFactor': 0.6434,
                'windSpeed': 9.078202806995757
            },
            {
                'dateTime': '2018-01-01T09:00Z',
                'loadFactor': 0.6898,
                'windSpeed': 9.404565234328848
            },
            {
                'dateTime': '2018-01-01T10:00Z',
                'loadFactor': 0.7134,
                'windSpeed': 9.57096697539607
            },
            {
                'dateTime': '2018-01-01T11:00Z',
                'loadFactor': 0.7807,
                'windSpeed': 10.064927158387052
            },
            {
                'dateTime': '2018-01-01T12:00Z',
                'loadFactor': 0.8154,
                'windSpeed': 10.42836672172881
            },
            {
                'dateTime': '2018-01-01T13:00Z',
                'loadFactor': 0.7354,
                'windSpeed': 9.725466757127355
            },
            {
                'dateTime': '2018-01-01T14:00Z',
                'loadFactor': 0.626,
                'windSpeed': 8.96439682154551
            },
            {
                'dateTime': '2018-01-01T15:00Z',
                'loadFactor': 0.5856,
                'windSpeed': 8.732835243473785
            },
            {
                'dateTime': '2018-01-01T16:00Z',
                'loadFactor': 0.4518,
                'windSpeed': 7.9619658901013
            },
            {
                'dateTime': '2018-01-01T17:00Z',
                'loadFactor': 0.3743,
                'windSpeed': 7.4533974644223235
            },
            {
                'dateTime': '2018-01-01T18:00Z',
                'loadFactor': 0.4745,
                'windSpeed': 8.09660983854582
            },
            {
                'dateTime': '2018-01-01T19:00Z',
                'loadFactor': 0.6498,
                'windSpeed': 9.123450665003581
            },
            {
                'dateTime': '2018-01-01T20:00Z',
                'loadFactor': 0.7761,
                'windSpeed': 10.017698377743605
            },
            {
                'dateTime': '2018-01-01T21:00Z',
                'loadFactor': 0.8102,
                'windSpeed': 10.373948945304505
            },
            {
                'dateTime': '2018-01-01T22:00Z',
                'loadFactor': 0.8094,
                'windSpeed': 10.365416031257272
            },
            {
                'dateTime': '2018-01-01T23:00Z',
                'loadFactor': 0.7943,
                'windSpeed': 10.207992614384843
            }
        ],
        'last day': [
            {
                'dateTime': '2018-12-31T00:00Z',
                'loadFactor': 0.487,
                'windSpeed': 8.168352981468397
            },
            {
                'dateTime': '2018-12-31T01:00Z',
                'loadFactor': 0.4138,
                'windSpeed': 7.712388573892642
            },
            {
                'dateTime': '2018-12-31T02:00Z',
                'loadFactor': 0.3585,
                'windSpeed': 7.350093136044134
            },
            {
                'dateTime': '2018-12-31T03:00Z',
                'loadFactor': 0.3206,
                'windSpeed': 7.101581980194127
            },
            {
                'dateTime': '2018-12-31T04:00Z',
                'loadFactor': 0.3418,
                'windSpeed': 7.240429110603869
            },
            {
                'dateTime': '2018-12-31T05:00Z',
                'loadFactor': 0.3788,
                'windSpeed': 7.483197320774347
            },
            {
                'dateTime': '2018-12-31T06:00Z',
                'loadFactor': 0.4129,
                'windSpeed': 7.706619237528843
            },
            {
                'dateTime': '2018-12-31T07:00Z',
                'loadFactor': 0.4457,
                'windSpeed': 7.921660535054523
            },
            {
                'dateTime': '2018-12-31T08:00Z',
                'loadFactor': 0.4819,
                'windSpeed': 8.138727174023872
            },
            {
                'dateTime': '2018-12-31T09:00Z',
                'loadFactor': 0.5122,
                'windSpeed': 8.312362643124862
            },
            {
                'dateTime': '2018-12-31T10:00Z',
                'loadFactor': 0.5179,
                'windSpeed': 8.345258028653562
            },
            {
                'dateTime': '2018-12-31T11:00Z',
                'loadFactor': 0.5088,
                'windSpeed': 8.29320866496573
            },
            {
                'dateTime': '2018-12-31T12:00Z',
                'loadFactor': 0.4737,
                'windSpeed': 8.091771112463942
            },
            {
                'dateTime': '2018-12-31T13:00Z',
                'loadFactor': 0.4344,
                'windSpeed': 7.847797944218214
            },
            {
                'dateTime': '2018-12-31T14:00Z',
                'loadFactor': 0.4155,
                'windSpeed': 7.7238889700713385
            },
            {
                'dateTime': '2018-12-31T15:00Z',
                'loadFactor': 0.4007,
                'windSpeed': 7.626421131087601
            },
            {
                'dateTime': '2018-12-31T16:00Z',
                'loadFactor': 0.3968,
                'windSpeed': 7.601093662852224
            },
            {
                'dateTime': '2018-12-31T17:00Z',
                'loadFactor': 0.4226,
                'windSpeed': 7.770545804445805
            },
            {
                'dateTime': '2018-12-31T18:00Z',
                'loadFactor': 0.4654,
                'windSpeed': 8.044188088173541
            },
            {
                'dateTime': '2018-12-31T19:00Z',
                'loadFactor': 0.5183,
                'windSpeed': 8.347333678842729
            },
            {
                'dateTime': '2018-12-31T20:00Z',
                'loadFactor': 0.5352,
                'windSpeed': 8.44431431216017
            },
            {
                'dateTime': '2018-12-31T21:00Z',
                'loadFactor': 0.498,
                'windSpeed': 8.23116574122035
            },
            {
                'dateTime': '2018-12-31T22:00Z',
                'loadFactor': 0.4483,
                'windSpeed': 7.938895982393953
            },
            {
                'dateTime': '2018-12-31T23:00Z',
                'loadFactor': 0.4092,
                'windSpeed': 7.682292185167821
            }
        ],
        'statistics': {
            'load factor max': 0.9,
            'load factor min': 0,
            'load factor sum': 3153.602500000006,
            'total hours': 8760,
            'wind speed max': 18.415818396373766,
            'wind speed min': 0.599666555550963,
            'wind speed sum': 61387.16363691816
        }
    },
    'weatherYear summary': {
        'first day': [
            {
                'dateTime': '2018-01-01T00:00Z',
                'loadFactor': 0.4388,
                'windSpeed': 7.876560615368952
            },
            {
                'dateTime': '2018-01-01T01:00Z',
                'loadFactor': 0.3583,
                'windSpeed': 7.348971309108386
            },
            {
                'dateTime': '2018-01-01T02:00Z',
                'loadFactor': 0.3342,
                'windSpeed': 7.190998691430778
            },
            {
                'dateTime': '2018-01-01T03:00Z',
                'loadFactor': 0.3785,
                'windSpeed': 7.481275218581458
            },
            {
                'dateTime': '2018-01-01T04:00Z',
                'loadFactor': 0.4467,
                'windSpeed': 7.928409295955033
            },
            {
                'dateTime': '2018-01-01T05:00Z',
                'loadFactor': 0.5264,
                'windSpeed': 8.393605822280064
            },
            {
                'dateTime': '2018-01-01T06:00Z',
                'loadFactor': 0.5976,
                'windSpeed': 8.80148615075951
            },
            {
                'dateTime': '2018-01-01T07:00Z',
                'loadFactor': 0.6387,
                'windSpeed': 9.045089489432309
            },
            {
                'dateTime': '2018-01-01T08:00Z',
                'loadFactor': 0.6772,
                'windSpeed': 9.315890330434287
            },
            {
                'dateTime': '2018-01-01T09:00Z',
                'loadFactor': 0.7278,
                'windSpeed': 9.672225476738644
            },
            {
                'dateTime': '2018-01-01T10:00Z',
                'loadFactor': 0.7537,
                'windSpeed': 9.854210197874986
            },
            {
                'dateTime': '2018-01-01T11:00Z',
                'loadFactor': 0.8123,
                'windSpeed': 10.39558690090373
            },
            {
                'dateTime': '2018-01-01T12:00Z',
                'loadFactor': 0.8505,
                'windSpeed': 10.794985669380093
            },
            {
                'dateTime': '2018-01-01T13:00Z',
                'loadFactor': 0.7767,
                'windSpeed': 10.0233564298248
            },
            {
                'dateTime': '2018-01-01T14:00Z',
                'loadFactor': 0.6595,
                'windSpeed': 9.191820143531611
            },
            {
                'dateTime': '2018-01-01T15:00Z',
                'loadFactor': 0.6217,
                'windSpeed': 8.939680469465584
            },
            {
                'dateTime': '2018-01-01T16:00Z',
                'loadFactor': 0.4757,
                'windSpeed': 8.103390510836316
            },
            {
                'dateTime': '2018-01-01T17:00Z',
                'loadFactor': 0.3897,
                'windSpeed': 7.554411786866376
            },
            {
                'dateTime': '2018-01-01T18:00Z',
                'loadFactor': 0.5011,
                'windSpeed': 8.249108145340507
            },
            {
                'dateTime': '2018-01-01T19:00Z',
                'loadFactor': 0.6842,
                'windSpeed': 9.365246319384813
            },
            {
                'dateTime': '2018-01-01T20:00Z',
                'loadFactor': 0.8073,
                'windSpeed': 10.343751015542967
            },
            {
                'dateTime': '2018-01-01T21:00Z',
                'loadFactor': 0.8447,
                'windSpeed': 10.735127313476596
            },
            {
                'dateTime': '2018-01-01T22:00Z',
                'loadFactor': 0.8438,
                'windSpeed': 10.725743081411343
            },
            {
                'dateTime': '2018-01-01T23:00Z',
                'loadFactor': 0.8273,
                'windSpeed': 10.552701151726573
            }
        ],
        'last day': [
            {
                'dateTime': '2018-12-31T00:00Z',
                'loadFactor': 0.5147,
                'windSpeed': 8.326814073585819
            },
            {
                'dateTime': '2018-12-31T01:00Z',
                'loadFactor': 0.4323,
                'windSpeed': 7.8336978265260315
            },
            {
                'dateTime': '2018-12-31T02:00Z',
                'loadFactor': 0.3727,
                'windSpeed': 7.443181123302013
            },
            {
                'dateTime': '2018-12-31T03:00Z',
                'loadFactor': 0.3319,
                'windSpeed': 7.176006691892255
            },
            {
                'dateTime': '2018-12-31T04:00Z',
                'loadFactor': 0.3547,
                'windSpeed': 7.325210201612169
            },
            {
                'dateTime': '2018-12-31T05:00Z',
                'loadFactor': 0.3946,
                'windSpeed': 7.586516181414895
            },
            {
                'dateTime': '2018-12-31T06:00Z',
                'loadFactor': 0.4313,
                'windSpeed': 7.8274699059747705
            },
            {
                'dateTime': '2018-12-31T07:00Z',
                'loadFactor': 0.4681,
                'windSpeed': 8.059800240886311
            },
            {
                'dateTime': '2018-12-31T08:00Z',
                'loadFactor': 0.5091,
                'windSpeed': 8.294720761009858
            },
            {
                'dateTime': '2018-12-31T09:00Z',
                'loadFactor': 0.542,
                'windSpeed': 8.482921842604581
            },
            {
                'dateTime': '2018-12-31T10:00Z',
                'loadFactor': 0.5482,
                'windSpeed': 8.518604677507238
            },
            {
                'dateTime': '2018-12-31T11:00Z',
                'loadFactor': 0.5383,
                'windSpeed': 8.462148899997782
            },
            {
                'dateTime': '2018-12-31T12:00Z',
                'loadFactor': 0.5002,
                'windSpeed': 8.243868810360723
            },
            {
                'dateTime': '2018-12-31T13:00Z',
                'loadFactor': 0.4546,
                'windSpeed': 7.979953986316166
            },
            {
                'dateTime': '2018-12-31T14:00Z',
                'loadFactor': 0.4342,
                'windSpeed': 7.846113221243828
            },
            {
                'dateTime': '2018-12-31T15:00Z',
                'loadFactor': 0.4181,
                'windSpeed': 7.7409275475044845
            },
            {
                'dateTime': '2018-12-31T16:00Z',
                'loadFactor': 0.414,
                'windSpeed': 7.713608336118387
            },
            {
                'dateTime': '2018-12-31T17:00Z',
                'loadFactor': 0.4419,
                'windSpeed': 7.896494074292405
            },
            {
                'dateTime': '2018-12-31T18:00Z',
                'loadFactor': 0.4912,
                'windSpeed': 8.192356778739773
            },
            {
                'dateTime': '2018-12-31T19:00Z',
                'loadFactor': 0.5486,
                'windSpeed': 8.520856508248654
            },
            {
                'dateTime': '2018-12-31T20:00Z',
                'loadFactor': 0.567,
                'windSpeed': 8.62610789073937
            },
            {
                'dateTime': '2018-12-31T21:00Z',
                'loadFactor': 0.5266,
                'windSpeed': 8.394882597365951
            },
            {
                'dateTime': '2018-12-31T22:00Z',
                'loadFactor': 0.4713,
                'windSpeed': 8.078438689075705
            },
            {
                'dateTime': '2018-12-31T23:00Z',
                'loadFactor': 0.4273,
                'windSpeed': 7.801212404394793
            }
        ],
        'statistics': {
            'load factor max': 0.9,
            'load factor min': 0,
            'load factor sum': 3235.452200000011,
            'total hours': 8760,
            'wind speed max': 19.756298144292863,
            'wind speed min': 0.5188365763137381,
            'wind speed sum': 62368.276615883166
        }
    }
}
