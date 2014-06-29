logger = Ember.Logger;

Ember.onerror = function(error) {
    logger.log(error);
    throw error;
};

var windowShowEvent = $.Callbacks();
var windowHideEvent = $.Callbacks();

App = Ember.Application.create({
    tray: null,
    ready: function() {
        logger.log("app is ready");
        var me = this;
        var tray = Ti.UI.addTray("app://app_logo.png", function() {
            me.trayClicked();
        });
        this.set("tray", tray);
        var w = Ti.UI.getMainWindow();
        w.addEventListener(Ti.UNFOCUSED, function() {
            me.lostFocus();
        });
        this.moveToCorner();
        this.hideWindow();
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
        w.moveTo(wwidth - width, wheight - height);
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

App.ApplicationController = Ember.Controller.extend({


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
        }, 1000));
    },
    deactivate: function() {
        windowShowEvent.remove(this.get("showEvent"));
        window.clearInterval(this.get("update"));
    },
    update: null,
    showEvent: null
});

App.ChatRoute = Ember.Route.extend({
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








// Widgets, TODO: cambiar a archivo separado

Ws = Em.Namespace.create();

Ws.FocusableTextField = Em.TextField.extend({
    didInsertElement: function() {
        this.$().focus();
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