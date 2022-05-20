# ====================================================
# attention->LSTMに変更
# ====================================================
class LSTMModel(nn.Module):
    def __init__(self, cfg, config_path=None, pretrained=False):
        super().__init__()
        self.cfg = cfg
        self.model_name = "LSTM"
        if config_path is None:
            self.config = AutoConfig.from_pretrained(cfg.model, output_hidden_states=True)
        else:
            self.config = torch.load(config_path)
        if pretrained:
            self.model = AutoModel.from_pretrained(cfg.model, config=self.config)
        else:
            self.model = AutoModel.from_config(self.config)
        # self.fc_dropout = nn.Dropout(cfg.fc_dropout)
        self.fc_bn = nn.BatchNorm1d(self.config.hidden_size)  # TODO サイズあってるか確認
        self.fc = nn.Linear(self.config.hidden_size, self.cfg.target_size)
        self.lstm = nn.LSTM(self.config.hidden_size, self.config.hidden_size, batch_first=True)
        self._init_weights(self.fc)
        self._init_weights(self.attention)
        
    def _init_weights(self, module):
        if isinstance(module, nn.Linear):
            module.weight.data.normal_(mean=0.0, std=self.config.initializer_range)
            if module.bias is not None:
                module.bias.data.zero_()
        elif isinstance(module, nn.Embedding):
            module.weight.data.normal_(mean=0.0, std=self.config.initializer_range)
            if module.padding_idx is not None:
                module.weight.data[module.padding_idx].zero_()
        elif isinstance(module, nn.LayerNorm):
            module.bias.data.zero_()
            module.weight.data.fill_(1.0)

    def forward(self, inputs):
        outputs = self.model(**inputs)
        last_hidden_states = outputs[0]
        # feature = torch.mean(last_hidden_states, 1)
        out, _ = self.lstm(last_hidden_states, None)
        sequence_output = out[:, -1, :]
        logits = self.fc(sequence_output)
        return logits