from ScriptingBridge import SBApplication


app = SBApplication.applicationWithBundleIdentifier_('com.googlecode.iterm2')
win = app.createWindowWithDefaultProfileCommand_('/bin/bash')
ses = win.currentSession()
ses.setName_('foo')
ses.writeContentsOfFile_text_newline_(None, 'pwd', True)

tab = win.createTabWithDefaultProfileCommand_('/bin/bash')
ses = tab.currentSession()
ses.setName_('bar')
ses.writeContentsOfFile_text_newline_(None, 'ls', True)

tab = win.createTabWithDefaultProfileCommand_('/bin/bash')
ses = tab.currentSession()
ses.setName_('baz 1')
ses.writeContentsOfFile_text_newline_(None, 'echo 1', False)

# Split into 5 panes.
for i in range(2, 6):
    ses = ses.splitHorizontallyWithDefaultProfileCommand_('/bin/bash')
    ses.setName_('baz {}'.format(i))
    ses.writeContentsOfFile_text_newline_(None, 'echo {}'.format(i), False)
