const { createApp } = Vue

const app = {
  data() {
    return {
      menuItems: [
        {name: "Top of page", url: ""},
        {name: "Contacts", url:"contact"},
        {name: "Work Experience", url: "experience"},
        {name: "Education", url:"education"},
        {name: "Projects", url:"project"},
        {name: "Technologies and Skills", url:"tech"}
      ]
    }
  },
  delimiters: ['{', '}'],
}

const component = {
  data() {
    return {
      componentKey: 0,
    }
  },
  methods: {
    reload(){
      this.componentKey++;
    }
  },
  delimiters: ['{', '}'],
}

createApp(app).mount('#app')