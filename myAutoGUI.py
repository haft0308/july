#import pywinauto

from pywinauto.application import Application
from pywinauto import findwindows
import time
from pywinauto.keyboard import send_keys

# app = Application(backend='uia')

# procs = findwindows.find_elements()#현재 윈도우 화면에 있는 프로세스 목록 리스트.
# print(len(procs))#몇개의 프로세스가 있는지 알려주고,
# for process in procs:
#     #print(f"{process} / 프로세스 : {process.control_id}, {process.framework_id} , {process.auto_id} ")#프로세스 정보를 출력하자
#     print(f"{process} / 프로세스 : {process.control_id}")
#app.start("notepad.exe")
# app.start("C:\\windows\\notepad.exe")
#app.connect(title_re = "notepad.exe")
#app.connect(process=28294)
#
#app.UntitledNotepad.Edit.type_keys("iot iot!", with_spaces = True)
# time.sleep(10)
#컨트롤 요소 출력
#dlg = app['C:\\windows\\notepad.exe']#메모장

# notepad = app.window(title_re = ".*메모장")
# notepad.set_focus()#포커스를 메모장으로

#dlg.print_control_identifiers()#메모장의 컨트롤 요소를 트리로 모두 출력

# send_keys("되나?")#실제 키보드 입력처럼 보이게 타이핑
# send_keys("됨!")



# from pywinauto.application import Application
#
# # 응용 프로그램 시작
# app = Application().start('notepad.exe')
# # time.sleep(1)
#
#
# # 'Untitled - Notepad' 윈도우 선택
# dlg = app.window(title_re=".*메모장")
#
# dlg.wait('visible', timeout=10)
# dlg.wait_not('exists', timeout=30)
# # 'Edit' 컨트롤에 텍스트 입력
# dlg.Edit.type_keys("Hello, PyWinAuto!", with_spaces=True)
#
# # 메뉴에서 'File->Exit' 선택
# dlg.menu_select("File->Exit")
#
# # 'Notepad' 대화 상자에서 'Don't Save' 버튼 클릭
# app.Notepad.Dialog.DontSave.click()

from pywinauto import Application
import pywinauto


application = Application(backend="uia")
app_start = application.start("notepad.exe")
dlg = app_start.window(title_re="Untitled")  # 한글 윈도우 환경 고려
#notepad.set_focus(True)

dlg.wait('ready', timeout=15)
dlg.set_focus()

dlg.type_keys("Hello, world!", with_spaces=True)
