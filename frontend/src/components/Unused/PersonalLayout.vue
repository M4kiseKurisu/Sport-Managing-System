<template>
    <div class="personalInformation">
        <personalInformation />
    </div>
    <div class="activeRate">
        <activeRate />
    </div>
</template>

<script>
import personalInformation from "./PersonalInformation.vue"
import activeRate from "./ActiveRate.vue"
export default {
    components: {
        personalInformation,
        activeRate
    }
}
</script>

<style scoped>
.personalInformation {
    padding-top: 36px;
    padding-left: 36px;
    float: left;
}

.activeRate {
    padding-top: 36px;
    margin-left: 36px;
    float: left;
}
</style>