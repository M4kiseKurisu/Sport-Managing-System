<template>
  <div id="app">
    <!-- <Login /> -->
    <MainPage />
  </div>
</template>

<script>
import Login from "./components/Login/Login.vue"
// import BasicLayout from "./components/BasicLayout.vue"
import MainPage from "./components/MainPage/MainPageContainer.vue"

export default {
  components: {
    Login,
    MainPage,
    // BasicLayout
  }
}
</script>

<style></style>