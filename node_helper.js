const NodeHelper = require("node_helper");
const fs = require("fs");
var pyshell = require('python-shell');

module.exports = NodeHelper.create({

  socketNotificationReceived: function (notification, payload) {
    if (notification === "START") {
      this.config = payload;
      this.kudagoGetData();
      this.readData();
      setInterval(() => {
        this.kudagoGetData();
        this.readData();
      }, this.config.updateInterval);
    }
  },

  readData: function () {
    //read a file with events
    fs.readFile("./modules/MMM-KudaGo/kudago/events.json", "utf8", (err, data) => {
      if (err) throw err;
      this.sendSocketNotification("DATA", data);
    });
  },

  kudagoGetData: function () {
    //call python script for collecting events from KudaGo api
    var options = {
      pythonPath: this.config.pythonPath,
      scriptPath: './modules/MMM-KudaGo/kudago',
      mode: 'json',
      args: [
        "--location", this.config.location,
        "--days", this.config.days,
        "--categories", this.config.categories
      ]
    };

    pyshell.PythonShell.run('kudago.py', options, function (err) {
      if (err) throw err;
    });
  },
});