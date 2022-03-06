from django.contrib import admin
from .models import Candidate


class CandidateAdmin(admin.ModelAdmin):
    exclude = ('creator','created_date','modified_date')
    list_display = (
        'username','city','bachelor_school','first_score','first_result','first_interviewer','second_result',
        'second_interviewer','hr_score','hr_result','last_editor'
    )

    # 筛选条件
    list_filter = ('city','first_result','second_result','hr_result','first_interviewer','second_interviewer','hr_interviewer')

    # 查询字段
    search_fields = ('username','phone','email','bachelor_school')

    # 默认排序
    ordering = ('hr_result','second_result','first_result')

    fieldsets = (
        (None,{'fields':("userid", ("username", "city"), ("phone", "email"), ("apply_position", "born_address"), ("gender", "candidate_remark"), ("bachelor_school", "master_school"), ("doctor_school", "major"), ("degree", "test_score_of_general_ability"), "paper_score")}),
        ('第一轮面试记录', {'fields': (("first_score", "first_learning_ability"), ("first_professional_competency", "first_advantage"), ("first_result", "first_recommend_position"), ("first_interviewer", "first_remark"))}),
        ('第二轮专业面试记录', {'fields': (("second_score", "second_learning_ablity"), ("second_professional_competency", "second_pursue_of_excellence"), ("second_communication_ability", "second_pressure_score"), ("second_davantage", "second_disadvantage"), ("second_result", "second_recommend_position"), ("second_interviewer", "second_remark"))}),
        ('第三轮HR面试记录', {'fields': (("hr_score", "hr_responsibility"), ("hr_communication_ability", "hr_logic_ability"), ("hr_porential", "hr_stability"), ("hr_advantage", "hr_disadvantage"), ("hr_result", "hr_interviewer"))}),
    )



admin.site.register(Candidate,CandidateAdmin)