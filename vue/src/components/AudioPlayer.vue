<template>
  <b-card header="Listen to your Beat">
    <audio
      style="display: block; width: 100%"
      class="mb-4"
      controls
      :src="src"
    >
      Your browser does not support the audio element.
    </audio>
    <b-button
      variant="danger"
      @click="$emit('back')"
    >
      Start Over
    </b-button>
  </b-card>
</template>

<script>
export default {
  props: {
    src: {
      type: String,
      required: true,
    },
  },
};
</script>
