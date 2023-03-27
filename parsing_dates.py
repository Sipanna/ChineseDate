from dates import ChineseDate, GregDate

date_str = "10.08.1985"
date = GregDate(date_str)
chinese_date = ChineseDate(date)

chinese_date.print_info()
