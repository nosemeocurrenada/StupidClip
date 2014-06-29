logger = Ember.Logger;

Ember.onerror = function(error) {
    logger.log(error);
    throw error;
};

var windowShowEvent = $.Callbacks();
var windowHideEvent = $.Callbacks();
var uniqueChatModelInstance;

App = Ember.Application.create({
    tray: null,
    ready: function() {
        logger.log("app is ready");
        logger.log("init python");
        window.py.init(Ti.Filesystem.getApplicationDataDirectory().nativePath());
        logger.log("python ready");

        var me = this;
        var tray = Ti.UI.addTray("app://assets/logo_min.png", function() {
            me.trayClicked();
        });
        this.set("tray", tray);
        var w = Ti.UI.getMainWindow();
        w.addEventListener(Ti.UNFOCUSED, function() {
            me.lostFocus();
        });
        this.moveToCorner();
        this.hideWindow();

        uniqueChatModelInstance = App.ChatModel.create();
    },
    trayClicked: function() {
        logger.log("tray icon clicked");
        var w = Ti.UI.getMainWindow();
        if (w.isVisible()) {
            this.hideWindow();
        } else
        if (this.lostFocusRecently) {
            logger.log("have lost focus recently, not showing");
        } else {
            this.moveToCorner();
            this.showWindow();
        }
    },
    hideWindow: function() {
        windowHideEvent.fire();
        logger.log("hidding window");
        var w = Ti.UI.getMainWindow();
        w.hide();
    },
    showWindow: function() {
        windowShowEvent.fire();
        logger.log("showing window");
        var w = Ti.UI.getMainWindow();
        w.show();
        w.focus();
        w.setTopMost(true);
        setTimeout(function() {
            w.setTopMost(false);
        }, 80);
    },
    moveToCorner: function() {
        logger.log("moviendo ventana");
        var w = Ti.UI.getMainWindow();
        var width = w.getWidth();
        var height = w.getHeight();
        var wwidth = window.screen.width;
        var wheight = window.screen.height;
        w.moveTo(wwidth - width, wheight - height - 30);
    },
    lostFocusRecently: false,
    lostFocus: function() {
        windowHideEvent.fire();
        this.set("lostFocusRecently", true);
        logger.log("lost focus");
        var w = Ti.UI.getMainWindow();
        w.setTopMost(false);
        logger.log("hidding");
        w.hide();
        var me = this;
        setTimeout(function() {
            me.set("lostFocusRecently", false);
        }, 800);
    }
});

App.Router.map(function() {
    this.route("idle");
    this.route("chat");
    this.route("options");
    this.route("notification");
});

App.IndexRoute = Ember.Route.extend({
    beforeModel: function() {
        this.transitionTo('idle');
    }
});

function parseMsg(msg) {
    return {
        message: msg.message,
        timstamp: msg.timestamp.strftime("%H:%S"),
        isPc: msg.sender == "System"
    }
};


App.ChatModel = Ember.Object.extend({
    messages: [],
    lastMessages: [],
    init: function() {
        this.set("messages", []);
        logger.log("inicializando chat model");
        var msgs = window.py.get_all_msg();
        var me = this;
        msgs.forEach(function(e) {
            me.messages.pushObject(parseMsg(e));
        });
        var c = me.messages.length - 10;
        if (c > 0)
            me.messages.removeAt(0, c);
        logger.log("chat model correctamente inicializado");
    }
});








App.IdleRoute = Ember.Route.extend({
    activate: function() {
        //show event
        var me = this;
        this.set("showEvent", function() {
            logger.log("transisionando al chat");
            me.transitionTo("chat");
        });
        windowShowEvent.add(this.get("showEvent"));
        //update
        this.set("update", window.setInterval(function() {
            logger.log("idle update");

            window.py.update();

            var msgs = window.py.get_new_msg();

            if (msgs.length > 0) {
                try {
                    App.showWindow();

                    logger.log("hubo mensajes nuevos")
                    var m = me.modelFor("idle");
                    m.set("lastMessages", msgs);
                    msgs.forEach(function(e) {
                        m.messages.pushObject(parseMsg(e));
                    });
                    var c = m.messages.length - 10;
                    if (c > 0)
                        m.messages.removeAt(0, c);


                    windowShowEvent.remove(me.get("showEvent"));
                    me.transitionTo("notification");
                    //alert("hay mensajes nuevos");
                } catch (err) {
                    logger.log(err);
                }
            }

        }, 1000));
    },
    deactivate: function() {
        try {
            windowShowEvent.remove(this.get("showEvent"));
        } catch (err) {
            logger.log(err);
        }
        window.clearInterval(this.get("update"));

    },
    model: function() {
        return uniqueChatModelInstance;
    },
    update: null,
    showEvent: null
});

App.IdleController = Ember.Controller.extend({});


App.ChatRoute = Ember.Route.extend({
    activate: function() {
        var me = this;
        this.set("hideEvent", function() {
            logger.log("transisionando a idle");
            me.transitionTo("idle");
        });
        windowHideEvent.add(this.get("hideEvent"));
        //update
        this.set("update", window.setInterval(function() {
            logger.log("chat update");

            window.py.update();

            var msgs = window.py.get_new_msg();

            if (msgs.length > 0) {
                try {
                    logger.log("hubo mensajes nuevos")
                    var m = me.modelFor("chat");
                    m.set("lastMessages", msgs);
                    msgs.forEach(function(e) {
                        m.messages.pushObject(parseMsg(e));
                    });
                    var c = m.messages.length - 10;
                    if (c > 0)
                        m.messages.removeAt(0, c);

                    //alert("hay mensajes nuevos");
                } catch (err) {
                    logger.log(err);
                }
            }

        }, 1000));
    },
    deactivate: function() {
        windowHideEvent.remove(this.get("hideEvent"));
        window.clearInterval(this.get("update"));
    },
    update: null,
    hideEvent: null,
    model: function() {
        return uniqueChatModelInstance;
    },
    setupController: function(controller, m) {
        logger.log("seteando modelo del controlador");
        logger.debug("this is the controller: " + controller);
        logger.debug("model name: " + m.name);
        controller.set("model", m);
    }
});

App.ChatController = Ember.Controller.extend({
    actions: {
        sendCommand: function() {
            var cmd = this.get("command");
            this.set("command", "");
            window.py.cmd(cmd);
        }
    },
    command: ""
});

App.OptionsRoute = Ember.Route.extend({
    activate: function() {
        var me = this;
        this.set("hideEvent", function() {
            logger.log("transisionando a idle");
            me.transitionTo("idle");
        });
        windowHideEvent.add(this.get("hideEvent"));
    },
    deactivate: function() {
        windowHideEvent.remove(this.get("hideEvent"));
    },
    hideEvent: null
});

App.OptionsController = Ember.Controller.extend({
    actions: {
        closeApp: function() {
            logger.log("closing app");
            Ti.UI.getCurrentWindow().close();
        },
        testPython: function() {
            logger.log("python test");
            var s = window.py.cmd("");
            alert(s);
        }
    },
    init: function() {
        logger.log("agregando handler de hide")
        windowHideEvent.add(function() {
            logger.log("got hidden");
        });
        windowShowEvent.add(function() {
            logger.log("got shown");
        });
    }
});

//

App.NotificationRoute = Ember.Route.extend({
    model: function() {
        return uniqueChatModelInstance;
    },
    activate: function() {
        var me = this;
        //update
        this.set("update", window.setInterval(function() {
            logger.log("notification update");

            window.py.update();

            var msgs = window.py.get_new_msg();

            if (msgs.length > 0) {
                try {
                    logger.log("hubo mensajes nuevos")
                    var m = me.modelFor("chat");
                    m.set("lastMessages", msgs);
                    msgs.forEach(function(e) {
                        m.messages.pushObject(parseMsg(e));
                    });
                    var c = m.messages.length - 10;
                    if (c > 0)
                        m.messages.removeAt(0, c);

                    //alert("hay mensajes nuevos");
                } catch (err) {
                    logger.log(err);
                }
            }

        }, 1000));
    },
    deactivate: function() {
        window.clearInterval(this.get("update"));
    },
    update: null,
    actions: {
        hide: function() {
            logger.log("ocultadisimo");
            App.hideWindow();
        },
        showChat: function() {
            logger.log("mostrando chat");
            this.transitionTo("chat");
        }
    }
})






// Widgets, TODO: cambiar a archivo separado

Ws = Em.Namespace.create();

Ws.FocusableTextField = Em.TextField.extend({
    didInsertElement: function() {
        this.$().focus();
        this.$().attr("size", 39);
    },
    focusOut: function() {
        logger.log("focused out");
        this.sendAction('lostFocus');
    },
    keyPress: function(e) {
        logger.log("key pressed");
        if (e.charCode == 13)
            this.sendAction('enterPress');
    }
});