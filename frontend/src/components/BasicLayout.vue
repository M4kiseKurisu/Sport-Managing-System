<template>
    <div class="background">
        <div class="left">
            <leftLayout />
        </div>
        <div class="right">
            <div class="up">
                <upperLayout />
            </div>
        </div>

    </div>
</template>

<script>
import leftLayout from "./LeftLayout.vue"
import upperLayout from "./UpperLayout.vue"
export default {
    components: {
        leftLayout,
        upperLayout
    }
}
</script>

<style>
.background {
    /* position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    margin: 0;
    padding: 0;
    width: 100%;
    height: 100%; */
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
    width: 83%;
    margin-left: auto;
    background: white;
}

.up {
    width: 100%;
    height: 60px;
    background: lightgray;
}
</style>