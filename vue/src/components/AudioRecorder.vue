<template>
  <div>
    <b-alert
      :show="error"
      variant="danger"
    >
      {{ error }}
    </b-alert>
    <stop-button
      v-if="isRecording"
      @click="onStop"
    />
    <record-button
      v-if="isStopped"
      @click="onRecord"
    />
  </div>
</template>

<script>
// import toWav from 'audiobuffer-to-wav';
import Recorder from 'recorder-js';
import RecordButton from './RecordButton.vue';
import StopButton from './StopButton.vue';

const STATUS_STOPPED = 0;
const STATUS_RECORDING = 1;
const STATUS_STOPPING = 2;

export default {
  components: {
    StopButton,
    RecordButton,
  },
  data() {
    return {
      status: STATUS_STOPPED,
      error: null,
      recorder: null,
    };
  },
  computed: {
    isStopped() { return this.status === STATUS_STOPPED; },
    isRecording() { return this.status === STATUS_RECORDING; },
  },
  methods: {
    async onRecord() {
      const audioContext = new (window.AudioContext || window.webkitAudioContext)();
      this.recorder = new Recorder(audioContext);
      try {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        this.recorder.init(stream);
        await this.recorder.start();
        this.status = STATUS_RECORDING;
      } catch (e) {
        this.error = e;
      }
    },
    async onStop() {
      this.status = STATUS_STOPPING;
      try {
        const { blob } = await this.recorder.stop();
        this.$emit('done', new File([blob], 'browser-recording.wav'));
        this.status = STATUS_STOPPED;
      } catch (e) {
        this.error = e;
      }
    },
  },
};
</script>
