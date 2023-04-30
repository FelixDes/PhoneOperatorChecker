/**
 * plugins/index.js
 *
 * Automatically included in `./src/main.js`
 */

// Plugins
import {loadFonts} from './webfontloader'
import vuetify from './vuetify'
import VueTelInput from 'vue3-tel-input'
import 'vue3-tel-input/dist/vue3-tel-input.css'

const VueTelInputOptions = {
    mode: "international",
    onlyCountries: ['RU']
}

export function registerPlugins(app) {
    loadFonts()
    app.use(VueTelInput, VueTelInputOptions);
    app.use(vuetify)
}
