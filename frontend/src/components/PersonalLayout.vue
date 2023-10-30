<template>
    <div class="personalInformation">
        <personalInformation />
    </div>
</template>

<script>
import personalInformation from "./PersonalInformation.vue"
export default {
    components: {
        personalInformation
    }
}
</script>

<style scoped>
.personalInformation {
    padding-top: 36px;
    padding-left: 36px;
}
</style>