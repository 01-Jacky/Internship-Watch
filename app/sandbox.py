# class Job:
#     def __init__(self, title, company, location, date, url):
#         self.title = title
#         self.company = company
#         self.location = location
#         self.date = date
#         self.url = 'https://www.indeed.com' + url
#
#     def __str__(self):
#         return '{:<40} {:<50} {:<40} {}'.format(self.company, self.title, self.location, self.date)
#
#     def __eq__(self, other):
#         if self.title == other.title and self.company == other.company and self.date == other.date:
#             return True
#         else:
#             return False
#
#     def __hash__(self):
#         return hash((self.title, self.company, self.date, self.url))
#
# j1 = Job('intern','amazon','seattle','2 days ago','www.whatever.com')
# j2 = Job('intern2','amazon','seattle','2 days ago','www.whatever.com')
#
# map = {
#     j1:j1,
#     j2:j2,
# }
#
#
# print(j1 == j2)
# print(hash(j1))
# print(hash(j2))
# print(id(j1))
# print(id(j2))
# print(map[j1])

from module1 import foo

print(foo.bar)