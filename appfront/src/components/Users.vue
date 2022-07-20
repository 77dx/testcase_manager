<template>
<div>
  <div id="app">
    <h1>网站列表</h1>
    <div v-for="user in users">
      {{ user.account }}
    </div>
  </div>
</div>
</template>

<script>
new Vue({
  el: '#app',
  data () {
    return {
      users: null
    }
  },
  mounted () {
    axios
      .get('http://127.0.0.1:8000/api_userlist/')
      .then(response => (this.users = response.data.data))
      .catch(function (error) { // 请求失败处理
        console.log(error);
      });
  }
})
</script>
