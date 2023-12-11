<template>
    <el-switch v-model="show" class="switch" inline-prompt size="large"
        style="--el-switch-on-color: #13ce66; --el-switch-off-color: #1890ff" active-text="所有动态" inactive-text="你的动态" />
    <keep-alive>
        <ul v-infinite-scroll="load" class="infinite-list" style="overflow: auto">
            <ul v-infinite-scroll="load" class="infinite-list" style="overflow: auto">
                <MomentCard v-for="(stream, index) in displayedStreamList" :key="index" :stream="stream"
                    @delete-stream="removeStream" />
            </ul>
        </ul>
    </keep-alive>
</template>

<script>
import axios from 'axios';
import MomentCard from './Moments/MomentCard.vue';

export default {
    data ()
    {
        return {
            streamList: [],
            yourStreamList: [],
            cnt: 0,
            myName: JSON.parse( sessionStorage.getItem( "user_name" ) ),
            show: true
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
                    for ( let i = 0; i < this.streamList.length; i += 1 )
                    {
                        if ( this.streamList[ i ].owner.name == this.myName )
                        {
                            this.yourStreamList.push( this.streamList[ i ] );
                        }
                    }
                    console.log( this.streamList )
                }
            } );
        },
        removeStream ( deletedStream )
        {
            // 在这里更新 streamList，删除对应的数据
            const index = this.streamList.findIndex( stream => stream.id === deletedStream.id );
            const index1 = this.yourStreamList.findIndex( stream => stream.id === deletedStream.id );
            console.log( index )
            if ( index !== -1 )
            {
                this.streamList.splice( index, 1 );
                this.yourStreamList.splice( index1, 1 );
            }
        }
    },
    created ()
    {
        this.getList()
    },
    computed: {
        displayedStreamList ()
        {
            return this.show ? this.streamList : this.yourStreamList;
        }
    },
}
</script>

<style scoped>
.switch {
    padding: 0 20px;
    margin-bottom: 10px;
}
</style>