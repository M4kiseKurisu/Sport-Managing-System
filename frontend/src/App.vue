<template>
  <div id="app">
    <!-- <Login /> -->
    <!-- <MainPage /> -->
    <router-view></router-view>
  </div>
</template>

<script>
import Login from "./components/Login/Login.vue";
// import BasicLayout from "./components/BasicLayout.vue"
import MainPage from "./components/MainPage/MainPageContainer.vue";

export default {
  components: {
    Login,
    MainPage,
  },
};
</script>

<style></style>