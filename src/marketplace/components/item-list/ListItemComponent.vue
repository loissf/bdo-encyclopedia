<template>
  <div :grade="item.grade" class="item" :id="item.id.toString()">
    <img class="icon" :src="item.icon" alt="" />
    <span class="name">{{ enhancement?.name }}{{ item.name }}</span>
    <div class="price details-section">
      <label for="price-value">Base Price</label>
      <span class="value" id="price-value"
        ><img
          class="silver-icon"
          src="https:\\cdn.arsha.io/icons/1.png"
          alt=""
        />{{ price }}</span
      >
    </div>
    <div class="stock details-section">
      <label for="stock-value">In Stock</label>
      <span class="value" id="stock-value">{{ item.stock }}</span>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from "vue";
import { ListItem, SubListItem } from "@/models/Item";

const props = defineProps({
  item: {
    type: Object as () => ListItem | SubListItem,
    required: true,
  },
});

const price = computed(() => {
  const size = props.item.basePrice.toString().length;
  if (size > 9) {
    return parseFloat((props.item.basePrice / 1000000000).toFixed(2)) + " b";
  } else if (size > 6) {
    return parseFloat((props.item.basePrice / 1000000).toFixed(2)) + " M";
  } else if (size > 3) {
    return parseFloat((props.item.basePrice / 1000).toFixed(2)) + " k";
  }
});

function isSubListItem(item: any): item is SubListItem {
  if ((props.item as SubListItem).enhancement) {
    return true;
  }

  return false;
}

const enhancementNames: { [key: number]: string } = {
  16: "PRI",
  17: "DUO",
  18: "TRI",
  19: "TET",
  20: "PEN",
};

const enhancementSymbols: { [key: number]: string } = {
  16: "I",
  17: "II",
  18: "III",
  19: "IV",
  20: "V",
};

const enhancement = computed(() => {
  if (isSubListItem(props.item)) {
    const level = props.item.enhancement;
    if (props.item.mainCategory === 20) {
      return {
        name: `${enhancementNames[level + 15]}:`,
        symbol: enhancementSymbols[level + 15],
      };
    }
    if (level > 0 && level <= 15) {
      return {
        name: `+${level} `,
        symbol: `+${level} `,
      };
    } else if (level > 15 && level <= 20) {
      return {
        name: `${enhancementNames[level]}:`,
        symbol: enhancementSymbols[level],
      };
    }
  }
});
</script>

<style scoped lang="scss">
.item {
  display: grid;

  grid-template: "icon name price stock" 1fr / 1fr 5fr 2fr 2fr;

  border: 1px solid rgba(255, 255, 255, 0.115);
  border-radius: 4px;
  box-shadow: 0px 0px 6px 0px rgba(0, 0, 0, 0.75);

  background-color: rgb(35, 35, 35);

  padding: 0.25rem;

  align-items: center;

  .icon {
    grid-area: icon;

    padding: 0.25rem;
    height: 2.5rem;
    width: 2.5rem;

    background-color: rgba(0, 0, 0, 0.65);
  }

  .name {
    grid-area: name;
    padding: 0.5rem;

    text-align: left;
  }

  .price {
    grid-area: price;

    .silver-icon {
      height: 1.25rem;
      padding-right: 0.25rem;
    }
  }

  .stock {
    grid-area: stock;
  }

  .details-section {
    display: flex;
    flex-direction: column;

    justify-content: space-between;

    height: 100%;

    padding: 0 0.5rem;

    border-left: 1px solid rgb(70, 70, 70);

    label {
      text-align: left;
      font-size: 75%;
      color: rgba(255, 255, 255, 0.35);
    }

    .value {
      text-align: right;
    }
  }

  &[grade="0"] {
    .name {
      color: white;
    }
    .icon {
      border: 1px solid rgba(255, 255, 255, 0.6);
      box-shadow: 0px 0px 8px 0px rgba(255, 255, 255, 0.4);
    }
  }

  &[grade="1"] {
    .name {
      color: rgba(0, 128, 0);
    }
    .icon {
      border: 1px solid rgba(0, 128, 0, 0.6);
      box-shadow: 0px 0px 8px 0px rgba(0, 128, 0, 0.4);
    }
  }

  &[grade="2"] {
    .name {
      color: rgba(60, 110, 255);
    }
    .icon {
      border: 1px solid rgba(60, 110, 255, 0.6);
      box-shadow: 0px 0px 8px 0px rgba(60, 110, 255, 0.4);
    }
  }

  &[grade="3"] {
    .name {
      color: rgba(200, 200, 0);
    }
    .icon {
      border: 1px solid rgba(200, 200, 0, 0.6);
      box-shadow: 0px 0px 8px 0px rgba(200, 200, 0, 0.4);
    }
  }

  &[grade="4"] {
    .name {
      color: rgba(170, 0, 0);
    }
    .icon {
      border: 1px solid rgba(170, 0, 0, 0.6);
      box-shadow: 0px 0px 8px 0px rgba(170, 0, 0, 0.4);
    }
  }
}
</style>
