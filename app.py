import urwid

palette = [('reversed', 'standout', '')]


class ActionButton(urwid.Button):
    def __init__(self, caption, callback):
        super(ActionButton, self).__init__("")
        urwid.connect_signal(self, 'click', callback)
        self._w = urwid.AttrMap(urwid.SelectableIcon(caption),
                None, focus_map='reversed')

class Friend(urwid.WidgetWrap):
    def __init__(self, name):
        self.name = name
        super(Friend, self).__init__(
                ActionButton(name, self.chat))
        self.history = []

    def chat(self, button):
        app.conversation.set_text(['from ', self.name])
        #app.message = 'okay'
        #session = urwid.Text(['from ', button.label])
        #content = urwid.Edit('enter to send....')
        #app.open_box(urwid.LineBox(urwid.Pile([session, content])))

friends = [Friend('vivi'), Friend('kiki'), Friend('jojo')] 

class ConversationListBox(urwid.ListBox):
    def __init__(self):
        body = urwid.SimpleListWalker([message()])
        super(ConversationListBox, self).__init__(body)



class App(object):
    def __init__(self):
        self.contacts = urwid.Pile(friends)
        self.conversation = urwid.Text('...')
        self.message = urwid.Edit('ready to send')
        self.friend = None
        self.session = urwid.Pile([self.conversation, self.message])
        main = urwid.Columns([('fixed', 10, self.contacts), ('fixed', 20, self.session)], )
        # self.contents = ([('fixed', 10, contacts), ('fixed', 20, session)])
        self.top = urwid.Filler(main)

    def open_box(self, box):
        self.contents.append(box)


app = App()

urwid.MainLoop(app.top, palette).run()

