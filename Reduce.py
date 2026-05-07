# ఉదాహరణ: లిస్ట్‌లోని నంబర్లన్నింటినీ కూడటం
from functools import reduce

nums = [1, 2, 3]
total = reduce(lambda x, y: x + y, nums)

print(total) # అవుట్‌పుట్: 6 (అంటే 1+2+3)

#వివరణ: reduce అనేది వరుసగా నంబర్లను తీసుకుని, కూడుకుంటూ వెళ్లి చివరగా ఒక నంబర్‌ను ఇస్తుంది.