<template>
    <v-container class="fill-height">
        <v-app-bar :elevation="2">
            <v-app-bar-title class="text-center">Phone operator checker</v-app-bar-title>
        </v-app-bar>
        <v-responsive class="d-flex text-center fill-height">
            <v-col class="mt-10">
                <span class="align-start">Paste your phone number</span>
                <vue-tel-input @input="preparePhone" mode="international" class="mb-1"></vue-tel-input>
                <v-btn @click="submit" :disabled="!isValid" class="my-2">
                    Get provider
                </v-btn>
                <v-divider vertical v-if="resShow"></v-divider>
                <v-card elevation="2" v-if="resShow" class="d-flex mt-4 pa-3 flex-column">
                    <span>{{
                        current_provider === original_provider ? current_provider : `${original_provider} -> ${current_provider}`
                        }}</span>
                    <span>{{ region }}</span>
                </v-card>
                <Transition name="bounce">
                    <v-alert
                            v-if="errorShow"
                            type="error"
                            title="Error"
                            text="Input data isn't valid"
                    ></v-alert>
                </Transition>
            </v-col>
        </v-responsive>
    </v-container>
</template>

<script>
import {VueTelInput} from 'vue3-tel-input'
import 'vue3-tel-input/dist/vue3-tel-input.css'

export default {
    name: "PhoneChecker",
    components: {
        VueTelInput,
    },
    data: () => ({
        phone: null,
        isValid: false,

        resShow: false,
        errorShow: false,

        original_provider: '',
        current_provider: '',
        region: '',
    }),

    methods: {
        submit() {
            this.$root.doGet("/?phoneNumber=" + this.phone, {
                "Access-Control-Allow-Origin": "*",
                'Access-Control-Allow-Credentials': true,
            }).then((res) => {
                this.resShow = true
                this.errorShow = false

                this.current_provider = res.current_provider
                this.original_provider = res.original_provider
                this.region = res.region
            }).catch((e) => {
                this.errorShow = true
                setTimeout(() => {
                    this.errorShow = false
                }, 2000)
            })
        },
        preparePhone(phone, phoneObject) {
            this.isValid = phoneObject ? (phoneObject?.valid ?? false) : this.isValid
            if (phoneObject?.valid) {
                this.phone = phoneObject.nationalNumber
            }
        }
    }
}
</script>

<style scoped>
.bounce-enter-active {
    animation: bounce-in 0.3s;
}

.bounce-leave-active {
    animation: bounce-in 0.3s reverse;
}

@keyframes bounce-in {
    0% {
        transform: scale(0);
    }
    100% {
        transform: scale(1);
    }
}
</style>
