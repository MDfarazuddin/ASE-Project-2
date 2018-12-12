from django.urls import path ,include
from . import views
urlpatterns = [
	path('profile',views.Student_profile,name="Student_profile"),
	path('courses/<slug:slug>',views.Student_courses,name="student_courses"),
	path('profile/grade-sheet/<slug:slug>',views.Student_grade_sheet,name="student_grades"),
    path('<slug:slug>',views.Student_profile),
    path('courses/your_course/<slug:slug>',views.Student_course_page,name="student_course_page"),
    path('courses/your_course/to-do-assignments/<slug:slug>',views.Student_assignment_list,name="student_course_page_assignments"),
    path('courses/assignments/<slug:slug>',views.Student_assignment_list_1,name="assignments"),
    path('courses/marklist/<slug:slug>',views.Student_view_scores,name = 'marks'),
    path('course/announcements',views.view_announcements,name="view_announcements"),
    path('profile/attendance/<slug:slug>',views.view_attendance,name='view_attendance')
]
