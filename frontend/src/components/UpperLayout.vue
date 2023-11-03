<template>
    <div>
        <a href="javascript:;" class="notification" @click="notice"></a>
        <div class="username" v-text="username"></div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            username: "fybxjj"
        }
    },
    methods: {
        notice() {

        }
    },
}
</script>

<style scoped>
.notification {
    display: block;
    float: left;
    margin-left: 89%;
    margin-top: 22px;
    height: 20px;
    width: 20px;
    background-image: url(../images/notification.png);
    background-size: 100%, 100%;
    background-repeat: no-repeat;
    background-position: center;
}

.username {
    font-size: large;
    margin-left: 92%;
    padding-top: 18px;
}
</style>