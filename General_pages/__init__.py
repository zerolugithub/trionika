# from allure.pytest_plugin import MASTER_HELPER
#
#
# # providing decorators via allure.xxx instead of pytest.allure.xxx
# from allure import MASTER_HELPER
#
# __methods_to_provide = [
#     'step',
#     'attach',
#     'single_step',
#     'label',
#     'feature',
#     'story',
#     'severity',
#     'issue',
#     'dynamic_issue',
#     'testcase',
#     'environment',
#     'attach_type',
# ]
#
# for method in __methods_to_provide:
#     globals()[method] = getattr(MASTER_HELPER, method)
