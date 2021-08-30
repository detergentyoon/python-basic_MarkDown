# import travel.thailand # import 는 맨 뒷부분은 항상 모듈이나 패키지여야함. 클래스나 함수는 직접 import 할 수 없음
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# # from import 구문에서는 모듈이나 패키지, 클래스 함수 모두 import 가능 
# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

from travel import * 
trip_to = vietnam.VietnamPackage()
trip_to.detail()
trip_to = thailand.ThailandPackage()
trip_to.detail()