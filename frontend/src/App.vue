<template>
    <v-app>
        <v-main>
            <PhoneChecker/>
        </v-main>
    </v-app>
</template>

<script>
import PhoneChecker from "@/components/PhoneChecker.vue";
import axios from "axios";

export default {
    name: "App",
    components: {PhoneChecker},

    mounted() {
        this.$root.doGet = this.doGet
    },

    methods: {
        doGet(url, config) {
            return this._callRest(axios.get, url, config)
        },
        _callRest(method, url, payload, opt) {
            return new Promise((resolve, reject) => method("api" + url, payload, opt).then(res => {
                resolve(res.data)
            }).catch(e => {
                reject(e)
            }))
        },
    },
}

</script>
