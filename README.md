# Django-Datetime-formatter
date time format by time zone

## Requirement recommend
- Python >= 3.4
- Django >= 1.9.x

## Features
- Month of date time
- Month with zero of date time
- Day of date time
- Day with zero of date time
- Year of date time

### Default
- format Y-m-d H:M:S

### Usage
simple usage

```python
date_tiem = DateTime()
print('{}/{}/{}'.format(date_time.timezone_day_zero(), date_time.timezone_month_zero(), date_time.timezone_year()))
```
