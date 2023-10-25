<template>
    <div class="background" id="background">
        <!--
            <Input />
            <Create />
        -->
        <component :is="tabComponent" :onEvent="changeHandle"></component>
    </div>
</template>

<script>
    import Input from "./Input.vue"
    import Create from "./Create.vue"
    export default{
        components:{
            Input,
            Create
        },
        data(){
            return{
                tabComponent: "Input"
            }
        },
        methods:{
            changeHandle(data){
                this.tabComponent = data;
            }
        }
    }
</script>

<style scoped>
.background{
    position: fixed;
    top: 0; bottom: 0; left: 0; right: 0; margin: 0; padding: 0;
    /*background: linear-gradient(220.55deg, #FFDC99 0%, #FF62C0 100%);*/
    /*background: linear-gradient(0, rgba(61, 221, 61, 0.8) 0%,white 80%, white 100%);*/
    background-image: url(../images/wave2.png);
    background-repeat: no-repeat; background-position: bottom;
    width: 100%;
    height: 100%;
    overflow: hidden;
    background-size:auto 100%;
    display:flex; justify-content: center; align-items: center;
}
</style>