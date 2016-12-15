/**
 * Created by Jaeger on 2016/11/25.
 */

var API = 'https://api.github.com/';


var vm = new Vue({
  el: '#app',

  data: {
    columnCount: 5,
    members: []
  },

  computed: {
    memberCount: function () {
      return members.length;
    }
  },

  created: function () {
    this.getMembers();
  },

  methods: {
    getMembers: function () {
      var xhr = new XMLHttpRequest();
      var self = this;

      var url = API + 'orgs/itscoder/members';
      xhr.open('GET', url);

      xhr.onload = function () {
        self.members = JSON.parse(xhr.responseText);
      };

      xhr.send()
    }
  }
});
