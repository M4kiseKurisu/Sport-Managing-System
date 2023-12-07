<template>
    <ul v-infinite-scroll="load" class="infinite-list" style="overflow: auto">
        <MomentCard v-for="(stream, index) in streamList" :key="index" :stream="stream" />
        <el-divider />
    </ul>
</template>

<script>
import axios from 'axios';
import MomentCard from './Moments/MomentCard.vue';

export default {
    data ()
    {
        return {
            streamList: [],
            cnt: 0,
        }

    },
    components: {
        MomentCard
    },
    methods: {
        load ()
        {
            this.cnt += 2;
        },
        getList ()
        {
            axios( {
                method: "GET",
                url: "http://127.0.0.1:8000/api/stream/view",
                params: {
                    uid: sessionStorage.getItem( "uid" )
                }
            } ).then( ( result ) =>
            {
                if ( result.data.status )
                {
                    this.streamList = result.data.list
                    console.log( this.streamList )
                }
            } );
        }
    },
    created ()
    {
        this.getList()
    }
}
</script>