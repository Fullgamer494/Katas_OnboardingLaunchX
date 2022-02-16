from datetime import *
from dateutil.relativedelta import *
hoy = datetime.now()
print(hoy)

hoy = hoy + relativedelta(months=12, weeks=0, hours=0)

print(hoy)