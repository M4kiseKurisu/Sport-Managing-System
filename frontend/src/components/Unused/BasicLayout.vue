<template>
    <div class="background">
        <div class="left">
            <leftLayout />
        </div>
        <div class="right">
            <div class="up">
                <upperLayout />
            </div>
            <div class="main">
                <PersonalLayout />
            </div>
        </div>

    </div>
</template>

<script>
import leftLayout from "./LeftLayout.vue"
import upperLayout from "./UpperLayout.vue"
import PersonalLayout from "./PersonalLayout.vue"
export default {
    components: {
        leftLayout,
        upperLayout,
        PersonalLayout
    }
}
</script>

<style scoped>
.background {
    overflow: hidden;
    background: rgb(240, 240, 240);
}

.left {
    float: left;
    display: block;
    height: 100%;
    width: 17%;
    position: fixed;
    background: linear-gradient(220.55deg, #5D85A6 0%, #0E2C5E 100%);
}

.right {
    float: right;
    width: 83%;
    height: 100%;
}

.up {
    width: 100%;
    height: 60px;
    background: lightgray;
}
</style>