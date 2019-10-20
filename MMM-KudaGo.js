Module.register("MMM-KudaGo", {
    defaults: {
        location: "spb",
        categories: "concert",
        days: 7,
        nextEventInterval: 10000,  //interval for changing current text every 10 sec
        updateInterval: 6 * 3600 * 1000, //writes and reads the file every 6 hours
        animationSpeed: 2.5 * 1000,  // speed of text fading and changing in 2.5 sec
        pythonPath: 'python3'  // shell command or path to Python 3.6 (or higher) binary
    },

    start: function () {
        //started at module loading
        this.sendSocketNotification("START", this.config);
        this.activeItem = 0;  //index of current item, that showing on screen
        this.eventsItems = [];  //array of events from file
        this.updateDom(this.config.animationSpeed);
        this.startUpdateLoop();
    },

    startUpdateLoop: function () {
        //method caled in loop by nextEventInterval timeout
        setInterval(() => {
            this.updateEvents()
        }, this.config.nextEventInterval);
    },

    updateEvents: function () {
        this.updateDom(this.config.animationSpeed);
        this.activeItem++;
    },

    socketNotificationReceived: function (notification, payload) {
        if (notification === "DATA") {
            this.dataFile = JSON.parse(payload);
            var eventsItems = [];
            
            for (var i in this.dataFile) {
                var item = this.dataFile[i];
                eventsItems.push(item);
            }

            function compare(a, b) {
                if (a.date > b.date) {
                    return 1;
                } else if (a.date <= b.date) {
                    return -1;
                }
            }
            this.eventsItems = eventsItems.sort(compare);
            this.activeItem = 0;
        }
    },

    getDom: function () {
        if (this.activeItem >= this.eventsItems.length) {
            this.activeItem = 0;
        }

        var wrapper = document.createElement("div");

        if (this.eventsItems.length > 0) {
            // header row for event place
            const rowOne = document.createElement('tr');
            const placeEl = document.createElement('td');
            placeEl.innerText = this.eventsItems[this.activeItem].place;
            placeEl.align = 'center';
            placeEl.colSpan = 3;
            placeEl.className = "small dimmed";
            rowOne.appendChild(placeEl);
            // main row for name, date, price
            const rowTwo = document.createElement('tr');
            const titleEl = document.createElement('td');
            const dateEl = document.createElement('td');
            const priceEl = document.createElement('td');
            titleEl.innerText = this.eventsItems[this.activeItem].title;
            titleEl.align = 'left';
            dateEl.innerText = this.eventsItems[this.activeItem].date;
            dateEl.align = 'center';
            dateEl.className = "small dimmed";
            priceEl.innerText = this.eventsItems[this.activeItem].price;
            priceEl.align = 'center';
            priceEl.className = "small dimmed";
            rowTwo.appendChild(titleEl);
            rowTwo.appendChild(dateEl);
            rowTwo.appendChild(priceEl);

            const tableEl = document.createElement('table');
            tableEl.appendChild(rowOne);
            tableEl.appendChild(rowTwo);
            wrapper.appendChild(tableEl);
        } else {
            wrapper.innerHTML = "Loading...";
        }
        return wrapper;
    }
});