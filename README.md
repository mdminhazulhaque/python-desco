# Desco Prepaid CLI

Collect information about Desco Prepaid Accounts over CLI

## Usage

```
Usage: app.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  get-balance              Get balance and consumption
  get-customer-info        Get customer info
  get-monthly-consumption  Get monthly consumption
  get-recharge-history     Get recharge history
```

### Get Balance

```
$ python3 app.py get-balance -a 987654321
-----------------------  -------------------
accountNo                987654321
meterNo                  667788990011
balance                  1384.35
currentMonthConsumption  2020.49
readingTime              2022-07-19 00:00:00
-----------------------  -------------------
```

### Get Customer Info

```
$ python3 app.py get-customer-info -a 987654321
-------------------  --------------------------
accountNo            987654321
contactNo            01833000000
customerName         MR. JOHN DOE
feederName           Sector 11
installationAddress  H-42, R-7, SEC-13, UTTARA
installationDate     2019-06-23 00:00:00
meterNo              667788990011
phaseType            Single Phase Meter
registerDate         2019-06-23 00:00:00
sanctionLoad         6
tariffSolution       Category-A: Residential
meterModel           None
transformer          None
SDName               Turag
-------------------  --------------------------
```

### Get Recharge History

```
$ python3 app.py get-recharge-history -a 987654321
rechargeDate           totalAmount     vat    energyAmount
-------------------  -------------  ------  --------------
2022-07-14 06:59:49           2000   95.24         1923.81
2022-07-09 16:35:34           1000   47.62          521.1
2022-05-30 19:31:52           3000  142.86         2665.31
2022-04-21 10:57:38           1980   94.29         1904.57
2022-04-08 23:29:45           1000   47.62          741.5
2022-03-31 10:02:25            500   23.81          480.95
2022-03-01 13:33:16           2000   95.24         1703.41
2022-02-22 12:25:31           2970  141.43          432.46
```

### Get Monthly Consumption

```
$ python3 app.py get-monthly-consumption -a 987654321
month      consumedTaka    consumedUnit    maximumDemand
-------  --------------  --------------  ---------------
2022-01            9              2.401            0
2022-02          162.45          43.323            2.08
2022-03         2204.92         390.8              2.69
2022-04         1260.25         238.501            2.924
2022-05         1292.47         243.864            3.764
2022-06         2222.68         393.6              3.57
2022-07         3901.46         564.81             2.546
2022-08         2891.26         463.185            3.302
2022-09         2032.6          363.622            2.69
2022-10          735.81         148.695            1.8
2022-11         1223.71         232.408            3.486
```
