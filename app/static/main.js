const { createApp } = Vue

const app = {
  data() {
    return {
      menuItems: [
        {name: "Home", url: ""},
        {name: "Work Experience", url: "experience"},
        {name: "Education", url:"education"},
        {name: "Projects", url:"project"},
        {name: "Technologies and Skills", url:"tech"},
        {name: "Contacts", url:"contact"},
        {name: "Resume", url:"resume"},]
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