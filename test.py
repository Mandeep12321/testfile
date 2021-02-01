
Question 1

Answer
list = [12,13,5,6,7,5]
sum = sum(list)
print(sum)




Question 2

Answer


dict =	{
  "1": 5,
  "2": 10,
  "3": 100,
   "4": 40,
  "5": 50,
  "6": 70
}
key = max(dict, key=dict.get) 
value = dict[key]

result = {

key:value

}
print(result)




Question 3

Answer

from itertools import groupby 

list = [0,0,0,1,1,1,0,0,0,1,1,0,1,1,1,1,0,0,1,1]
temp = groupby(list) 
res = max(temp, key = lambda sub: len(list(sub[1]))) 
print("Output of the above array would be : " + str(res[0])) 





Question 4 (a)

Answer

CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
    PRIMARY KEY (`id`),
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE `addresses` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `street` varchar(255) NOT NULL,
  `pincode` varchar(255) NOT NULL,
  `country` varchar(255) NOT NULL,
  `state` varchar(255) NOT NULL,
  `phone_number` varchar(255) NOT NULL,
  `created_by_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_addresses` (`created_by_id`),
  CONSTRAINT `fk_addresses_created_by_id` FOREIGN KEY (`created_by_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



Question 4 (b)

Answer

urlpatterns = [
    path('', RegistrationView, name='employee_insert'),
    path('list/',employee_list , name='employee_list'),
    path('delete/<int:id>',employee_delete, name ="employee_delete"),
    path('<int:id>/',employee_update,name='employee_update'),
    path('remove/<int:id>/', remove,name='remove'),
    path('login/',employee_login , name='employee_login'),

]


