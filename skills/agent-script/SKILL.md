---
name: agent-script
description: Agentforce Agent Script language reference for building AI agents — syntax, blocks, variables, flow control, patterns, and examples
scope: AGENTFORCE_SCRIPT_BUILDER
---

# <span data-proof="authored" data-by="ai:claude">Agentforce Agent Script Reference</span>

**<span data-proof="authored" data-by="ai:claude">SCOPE: AGENTFORCE_SCRIPT_BUILDER</span>** <span data-proof="authored" data-by="ai:claude">- This skill applies to building Agentforce agents using Agent Script.
**Use when:**</span> <span data-proof="authored" data-by="ai:claude">Creating, modifying, or debugging Agent Script files for Agentforce Builder or Agentforce DX.</span>

***

<span data-proof="authored" data-by="ai:claude">Agent Script is Salesforce's domain-specific language for creating agents in Agentforce. It combines deterministic logic with LLM reasoning to build predictable, context-aware agent workflows.</span>

## <span data-proof="authored" data-by="ai:claude">Language Characteristics</span>

### <span data-proof="authored" data-by="ai:claude">Two Instruction Types</span>

<span data-proof="authored" data-by="ai:claude">Agent Script uses two distinct instruction markers:</span>

| <span data-proof="authored" data-by="ai:claude">Marker</span> | <span data-proof="authored" data-by="ai:claude">Type</span>                   | <span data-proof="authored" data-by="ai:claude">Behavior</span>                                                                                         |
| ------------------------------------------------------------- | ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <span data-proof="authored" data-by="ai:claude">`->`</span>   | **<span data-proof="authored" data-by="ai:claude">Logic instruction</span>**  | <span data-proof="authored" data-by="ai:claude">Executes deterministically — business rules, actions, variable assignment, conditional branching</span> |
| <span data-proof="authored" data-by="ai:claude">`|`</span>    | **<span data-proof="authored" data-by="ai:claude">Prompt instruction</span>** | <span data-proof="authored" data-by="ai:claude">Natural language sent to the LLM for conversational handling</span>                                     |

```
reasoning:
  -> set @variables.order_count = @variables.order_count + 1
  | Please help the customer with their order inquiry.
  | The customer's name is {!@variables.customer_name}.
```

### <span data-proof="authored" data-by="ai:claude">Syntax Fundamentals</span>

* **<span data-proof="authored" data-by="ai:claude">Properties:</span>**<span data-proof="authored" data-by="ai:claude"></span> <span data-proof="authored" data-by="ai:claude">`key: value`</span> <span data-proof="authored" data-by="ai:claude">format</span>

* **<span data-proof="authored" data-by="ai:claude">Indentation:</span>** <span data-proof="authored" data-by="ai:claude">Whitespace-sensitive (consistent spaces or tabs required)</span>

* **<span data-proof="authored" data-by="ai:claude">Comments:</span>**<span data-proof="authored" data-by="ai:claude"></span> <span data-proof="authored" data-by="ai:claude">`#`</span> <span data-proof="authored" data-by="ai:claude">for single-line comments</span>

* **<span data-proof="authored" data-by="ai:claude">Resource references:</span>**<span data-proof="authored" data-by="ai:claude"></span> <span data-proof="authored" data-by="ai:claude">`@`</span> <span data-proof="authored" data-by="ai:claude">prefix —</span> <span data-proof="authored" data-by="ai:claude">`@actions.foo`,</span> <span data-proof="authored" data-by="ai:claude">`@topic.bar`,</span> <span data-proof="authored" data-by="ai:claude">`@variables.baz`</span>

* **<span data-proof="authored" data-by="ai:claude">Variable interpolation in prompts:</span>**<span data-proof="authored" data-by="ai:claude"></span> <span data-proof="authored" data-by="ai:claude">`{!@variables.variable_name}`</span>

* **<span data-proof="authored" data-by="ai:claude">Multiline strings:</span>** <span data-proof="authored" data-by="ai:claude">Use pipe</span> <span data-proof="authored" data-by="ai:claude">`|`</span> <span data-proof="authored" data-by="ai:claude">with indentation</span>

* **<span data-proof="authored" data-by="ai:claude">Slot-fill token:</span>**<span data-proof="authored" data-by="ai:claude"></span> <span data-proof="authored" data-by="ai:claude">`...`</span> <span data-proof="authored" data-by="ai:claude">triggers LLM to fill in a value</span>

### <span data-proof="authored" data-by="ai:claude">Operators</span>

| <span data-proof="authored" data-by="ai:claude">Operator</span>      | <span data-proof="authored" data-by="ai:claude">Purpose</span>        |
| -------------------------------------------------------------------- | --------------------------------------------------------------------- |
| <span data-proof="authored" data-by="ai:claude">`==`</span>          | <span data-proof="authored" data-by="ai:claude">Equal to</span>       |
| <span data-proof="authored" data-by="ai:claude">`!=`</span>          | <span data-proof="authored" data-by="ai:claude">Not equal to</span>   |
| <span data-proof="authored" data-by="ai:claude">`>`</span>           | <span data-proof="authored" data-by="ai:claude">Greater than</span>   |
| <span data-proof="authored" data-by="ai:claude">`<`</span>           | <span data-proof="authored" data-by="ai:claude">Less than</span>      |
| <span data-proof="authored" data-by="ai:claude">`+`</span>           | <span data-proof="authored" data-by="ai:claude">Addition</span>       |
| <span data-proof="authored" data-by="ai:claude">`-`</span>           | <span data-proof="authored" data-by="ai:claude">Subtraction</span>    |
| <span data-proof="authored" data-by="ai:claude">`is None`</span>     | <span data-proof="authored" data-by="ai:claude">Null check</span>     |
| <span data-proof="authored" data-by="ai:claude">`is not None`</span> | <span data-proof="authored" data-by="ai:claude">Not null check</span> |

***

## <span data-proof="authored" data-by="ai:claude">Agent Script Blocks</span>

<span data-proof="authored" data-by="ai:claude">Every agent is composed of these structural blocks:</span>

### <span data-proof="authored" data-by="ai:claude">system Block</span>

<span data-proof="authored" data-by="ai:claude">Contains welcome and error messages (both</span> **<span data-proof="authored" data-by="ai:claude">mandatory</span>**<span data-proof="authored" data-by="ai:claude">).</span>

```
system:
  welcome:
    | Welcome! How can I help you today, {!@variables.userPreferredName}?
  error:
    | I'm sorry, something went wrong. Please try again.
```

### <span data-proof="authored" data-by="ai:claude">config Block</span>

<span data-proof="authored" data-by="ai:claude">Defines agent identity and parameters.</span>

```
config:
  developer_name: my_support_agent
  label: Customer Support Agent
  description: Handles customer service inquiries
  type: AgentforceServiceAgent
  version: 1.0
  company: Acme Corp
  role: Customer Service Representative
```

**<span data-proof="authored" data-by="ai:claude">Agent types:</span>**

* <span data-proof="authored" data-by="ai:claude">`AgentforceServiceAgent`</span> <span data-proof="authored" data-by="ai:claude">— customer-facing</span>

* <span data-proof="authored" data-by="ai:claude">`AgentforceEmployeeAgent`</span> <span data-proof="authored" data-by="ai:claude">— internal employee-facing</span>

### <span data-proof="authored" data-by="ai:claude">variables Block</span>

<span data-proof="authored" data-by="ai:claude">Global variable declarations (see Variables section below).</span>

```
variables:
  customer_name: mutable string
  order_id: mutable string
  is_verified: mutable boolean = False
  num_turns: mutable number = 0
```

### <span data-proof="authored" data-by="ai:claude">language Block</span>

<span data-proof="authored" data-by="ai:claude">Specifies supported languages for the agent.</span>

```
language:
  - en_US
  - es_MX
```

### <span data-proof="authored" data-by="ai:claude">connection Block</span>

<span data-proof="authored" data-by="ai:claude">External integration configuration (required for</span> <span data-proof="authored" data-by="ai:claude">`@utils.escalate`).</span>

```
connection:
  messaging:
    outbound_route_type: queue
    outbound_route_name: Support_Queue
```

### <span data-proof="authored" data-by="ai:claude">topic Block</span>

<span data-proof="authored" data-by="ai:claude">Core logic container — instructions, actions, and reasoning for a specific domain.</span>

```
topic order_status:
  description: Handles order status inquiries
  reasoning:
    -> run @actions.get_order with order_id: @variables.order_id
       set @variables.order_details = @outputs.order_info
    | The order status is {!@variables.order_details}.
```

### <span data-proof="authored" data-by="ai:claude">start_agent Block</span>

<span data-proof="authored" data-by="ai:claude">The</span> **<span data-proof="authored" data-by="ai:claude">entry point</span>** <span data-proof="authored" data-by="ai:claude">for every conversation. Handles topic classification and routing.</span>

```
start_agent:
  description: Routes customer to the right topic
  reasoning:
    -> set @variables.num_turns = @variables.num_turns + 1
    | Classify the customer's request and route to the appropriate topic.
  actions:
    - @topic.order_status
    - @topic.returns
    - @topic.general_questions
```

### <span data-proof="authored" data-by="ai:claude">model_config Block</span>

<span data-proof="authored" data-by="ai:claude">Customize the model used by subagents.</span>

```
model_config:
  classifier:
    model: EinsteinHyperClassifier
```

**<span data-proof="authored" data-by="ai:claude">Note:</span>**<span data-proof="authored" data-by="ai:claude"></span> <span data-proof="authored" data-by="ai:claude">`EinsteinHyperClassifier`</span> <span data-proof="authored" data-by="ai:claude">offers faster classification but cannot support images or certain utilities.</span>

***

## <span data-proof="authored" data-by="ai:claude">Variables</span>

### <span data-proof="authored" data-by="ai:claude">Regular Variables</span>

<span data-proof="authored" data-by="ai:claude">Mutable variables with optional defaults.</span>

```
variables:
  name: mutable string = "John Doe"
  age: mutable number = 25
  is_active: mutable boolean = True
  start_date: mutable date = 2025-01-15
  order: mutable object = {"SKU": "abc123"}
  scores: list[number] = [95, 87.5, 92]
  record_id: mutable id
```

**<span data-proof="authored" data-by="ai:claude">Supported types:</span>**<span data-proof="authored" data-by="ai:claude"></span> <span data-proof="authored" data-by="ai:claude">`string`,</span> <span data-proof="authored" data-by="ai:claude">`number`,</span> <span data-proof="authored" data-by="ai:claude">`boolean`,</span> <span data-proof="authored" data-by="ai:claude">`date`,</span> <span data-proof="authored" data-by="ai:claude">`id`,</span> <span data-proof="authored" data-by="ai:claude">`object`,</span> <span data-proof="authored" data-by="ai:claude">`list[type]`</span>

### <span data-proof="authored" data-by="ai:claude">Linked Variables</span>

<span data-proof="authored" data-by="ai:claude">Value tied to an action's output. Cannot have defaults, cannot be objects or lists.</span>

```
variables:
  order_status:
    linked: @actions.get_order.status
    type: string
    description: Current order status from lookup
```

**<span data-proof="authored" data-by="ai:claude">Supported types:</span>**<span data-proof="authored" data-by="ai:claude"></span> <span data-proof="authored" data-by="ai:claude">`string`,</span> <span data-proof="authored" data-by="ai:claude">`number`,</span> <span data-proof="authored" data-by="ai:claude">`boolean`,</span> <span data-proof="authored" data-by="ai:claude">`date`,</span> <span data-proof="authored" data-by="ai:claude">`id`</span>

### <span data-proof="authored" data-by="ai:claude">System Variables</span>

<span data-proof="authored" data-by="ai:claude">Read-only, predefined. Access via</span> <span data-proof="authored" data-by="ai:claude">`@system_variables.<name>`.</span>

| <span data-proof="authored" data-by="ai:claude">Variable</span>                       | <span data-proof="authored" data-by="ai:claude">Description</span>                          |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| <span data-proof="authored" data-by="ai:claude">`@system_variables.user_input`</span> | <span data-proof="authored" data-by="ai:claude">The customer's most recent utterance</span> |

### <span data-proof="authored" data-by="ai:claude">Naming Rules</span>

* <span data-proof="authored" data-by="ai:claude">Start with a letter</span>

* <span data-proof="authored" data-by="ai:claude">Alphanumeric characters and underscores only</span>

* <span data-proof="authored" data-by="ai:claude">No trailing underscores or consecutive underscores</span>

* <span data-proof="authored" data-by="ai:claude">Maximum 80 characters</span>

***

## <span data-proof="authored" data-by="ai:claude">Conditional Expressions</span>

<span data-proof="authored" data-by="ai:claude">Agent Script supports</span> <span data-proof="authored" data-by="ai:claude">`if`</span> <span data-proof="authored" data-by="ai:claude">/</span> <span data-proof="authored" data-by="ai:claude">`else`</span> <span data-proof="authored" data-by="ai:claude">for deterministic branching.</span>

**<span data-proof="authored" data-by="ai:claude">Important:</span>** **<span data-proof="authored" data-by="ai:claude">`else if`</span><span data-proof="authored" data-by="ai:claude">is NOT supported.</span>**  <span data-proof="authored" data-by="ai:claude">Use nested</span> <span data-proof="authored" data-by="ai:claude">`if`</span> <span data-proof="authored" data-by="ai:claude">blocks or separate conditions.</span>

### <span data-proof="authored" data-by="ai:claude">Controlling Actions</span>

```
reasoning:
  -> if @variables.is_verified == True
    -> run @actions.get_account_details with id: @variables.account_id
       set @variables.account = @outputs.details
  -> else
    | Please verify your identity before I can access account details.
```

### <span data-proof="authored" data-by="ai:claude">Assigning Variables Conditionally</span>

```
reasoning:
  -> if @variables.order_total > 100
    -> set @variables.shipping = "free"
  -> else
    -> set @variables.shipping = "standard"
```

### <span data-proof="authored" data-by="ai:claude">Selecting Prompts</span>

```
reasoning:
  -> if @variables.is_vip == True
    | This is a VIP customer. Provide premium, personalized service.
  -> else
    | Provide standard customer service.
```

***

## <span data-proof="authored" data-by="ai:claude">Flow of Control</span>

### <span data-proof="authored" data-by="ai:claude">Execution Model</span>

1. **<span data-proof="authored" data-by="ai:claude">Every request starts at</span>** **<span data-proof="authored" data-by="ai:claude">`start_agent`</span>** <span data-proof="authored" data-by="ai:claude">— initializes variables, classifies topic</span>
2. **<span data-proof="authored" data-by="ai:claude">Instructions process top-to-bottom sequentially</span>**
3. **<span data-proof="authored" data-by="ai:claude">The LLM only reasons AFTER the full prompt is assembled</span>** <span data-proof="authored" data-by="ai:claude">— it does not see partial prompts</span>
4. **<span data-proof="authored" data-by="ai:claude">After a topic completes</span>**<span data-proof="authored" data-by="ai:claude">, the agent waits for the next utterance and returns to</span> <span data-proof="authored" data-by="ai:claude">`start_agent`</span>

### <span data-proof="authored" data-by="ai:claude">Processing Order Within a Topic</span>

1. <span data-proof="authored" data-by="ai:claude">Initialize an empty prompt</span>
2. <span data-proof="authored" data-by="ai:claude">Execute logic instructions (`->`) — increment counters, run actions, set variables</span>
3. <span data-proof="authored" data-by="ai:claude">Concatenate prompt instructions (`|`) to the prompt</span>
4. <span data-proof="authored" data-by="ai:claude">Evaluate conditional logic (`if`/`else`)</span>
5. <span data-proof="authored" data-by="ai:claude">Process</span> <span data-proof="authored" data-by="ai:claude">`after_reasoning`</span> <span data-proof="authored" data-by="ai:claude">instructions</span>
6. <span data-proof="authored" data-by="ai:claude">Send the complete prompt to the LLM</span>

### <span data-proof="authored" data-by="ai:claude">Topic Transitions</span>

<span data-proof="authored" data-by="ai:claude">Transitions using</span> <span data-proof="authored" data-by="ai:claude">`@utils.transition to`</span> <span data-proof="authored" data-by="ai:claude">are</span> **<span data-proof="authored" data-by="ai:claude">one-way</span>**<span data-proof="authored" data-by="ai:claude">:</span>

* <span data-proof="authored" data-by="ai:claude">Control does</span> **<span data-proof="authored" data-by="ai:claude">not</span>** <span data-proof="authored" data-by="ai:claude">return to the previous topic</span>

* <span data-proof="authored" data-by="ai:claude">The previous topic's prompt is</span> **<span data-proof="authored" data-by="ai:claude">discarded entirely</span>**

* <span data-proof="authored" data-by="ai:claude">The new topic reads from top to bottom, creating a fresh prompt</span>

```
reasoning:
  -> if @variables.needs_returns == True
    -> @utils.transition to @topic.returns
```

### <span data-proof="authored" data-by="ai:claude">Topic Delegation vs Transition</span>

| <span data-proof="authored" data-by="ai:claude">Method</span>                                                                        | <span data-proof="authored" data-by="ai:claude">Behavior</span>                                 | <span data-proof="authored" data-by="ai:claude">Returns?</span> |
| ------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| <span data-proof="authored" data-by="ai:claude">`@topic.foo`</span> <span data-proof="authored" data-by="ai:claude">(as tool)</span> | <span data-proof="authored" data-by="ai:claude">Delegates to topic, then comes back</span>      | <span data-proof="authored" data-by="ai:claude">Yes</span>      |
| <span data-proof="authored" data-by="ai:claude">`@utils.transition to @topic.foo`</span>                                             | <span data-proof="authored" data-by="ai:claude">One-way handoff, discards current prompt</span> | <span data-proof="authored" data-by="ai:claude">No</span>       |

***

## <span data-proof="authored" data-by="ai:claude">Tools (Reasoning Actions)</span>

<span data-proof="authored" data-by="ai:claude">Tools are actions available to the LLM to call</span> **<span data-proof="authored" data-by="ai:claude">at its discretion</span>**<span data-proof="authored" data-by="ai:claude">, unlike logic actions that always execute.</span>

### <span data-proof="authored" data-by="ai:claude">Defining Tools</span>

```
topic order_management:
  description: Manages customer orders
  reasoning:
    | Help the customer manage their orders.
  reasoning.actions:
    - name: check_status
      action: @actions.get_order_status
      description: Look up the current status of an order
      available when: @variables.order_id is not None
      with:
        order_id: @variables.order_id
      set:
        status: @variables.current_status
```

### <span data-proof="authored" data-by="ai:claude">Key Concepts</span>

* **<span data-proof="authored" data-by="ai:claude">Must wrap</span>** <span data-proof="authored" data-by="ai:claude">an action or</span> <span data-proof="authored" data-by="ai:claude">`@utils`</span> <span data-proof="authored" data-by="ai:claude">function</span>

* **<span data-proof="authored" data-by="ai:claude">`available when`</span>** <span data-proof="authored" data-by="ai:claude">— deterministically controls when the tool is visible to the LLM (hidden tools cannot be called)</span>

* **<span data-proof="authored" data-by="ai:claude">Naming and descriptions matter</span>** <span data-proof="authored" data-by="ai:claude">— the LLM uses them to decide whether to invoke a tool</span>

* **<span data-proof="authored" data-by="ai:claude">`with`</span>** <span data-proof="authored" data-by="ai:claude">— binds input parameters</span>

* **<span data-proof="authored" data-by="ai:claude">`set`</span>** <span data-proof="authored" data-by="ai:claude">— assigns output values to variables</span>

### <span data-proof="authored" data-by="ai:claude">Topic References as Tools</span>

```
reasoning.actions:
  # Delegates and returns control (like a function call)
  - name: check_shipping
    action: @topic.shipping_info

  # One-way transition (no return)
  - name: transfer_to_billing
    action: @utils.transition to @topic.billing
```

***

## <span data-proof="authored" data-by="ai:claude">Utils</span>

<span data-proof="authored" data-by="ai:claude">Three built-in utility functions:</span>

### <span data-proof="authored" data-by="ai:claude">@utils.transition to</span>

<span data-proof="authored" data-by="ai:claude">One-way topic switch. Executes immediately, halts current block.</span>

```
-> @utils.transition to @topic.returns
```

* <span data-proof="authored" data-by="ai:claude">No automatic return to the calling topic</span>

* <span data-proof="authored" data-by="ai:claude">Must explicitly create reverse transitions if needed</span>

* <span data-proof="authored" data-by="ai:claude">Useful for: order management, verification flows, routing based on variable state</span>

### <span data-proof="authored" data-by="ai:claude">@utils.set variable</span>

<span data-proof="authored" data-by="ai:claude">Sets a variable value using LLM interpretation.</span>

```
-> @utils.set variable @variables.customer_sentiment
   description: Determine whether the customer seems satisfied, neutral, or frustrated
   ...
```

<span data-proof="authored" data-by="ai:claude">The</span> <span data-proof="authored" data-by="ai:claude">`...`</span> <span data-proof="authored" data-by="ai:claude">token triggers the LLM to fill in the value based on the description.</span>

### <span data-proof="authored" data-by="ai:claude">@utils.escalate</span>

<span data-proof="authored" data-by="ai:claude">Escalates to a human agent via Omni-Channel.</span>

```
-> @utils.escalate
```

**<span data-proof="authored" data-by="ai:claude">Requirements:</span>**

* <span data-proof="authored" data-by="ai:claude">Active Omni-Channel connection</span>

* <span data-proof="authored" data-by="ai:claude">A</span> <span data-proof="authored" data-by="ai:claude">`connection`</span> <span data-proof="authored" data-by="ai:claude">block with</span> <span data-proof="authored" data-by="ai:claude">`outbound_route_type`</span> <span data-proof="authored" data-by="ai:claude">and</span> <span data-proof="authored" data-by="ai:claude">`outbound_route_name`</span>

* <span data-proof="authored" data-by="ai:claude">`escalate`</span> <span data-proof="authored" data-by="ai:claude">is a</span> **<span data-proof="authored" data-by="ai:claude">reserved keyword</span>** <span data-proof="authored" data-by="ai:claude">— cannot be used for topic or action names</span>

***

## <span data-proof="authored" data-by="ai:claude">Common Patterns</span>

### <span data-proof="authored" data-by="ai:claude">1. Action Chaining & Sequencing</span>

<span data-proof="authored" data-by="ai:claude">Execute multiple actions in guaranteed order:</span>

```
reasoning:
  -> run @actions.verify_identity with email: @variables.email
     set @variables.is_verified = @outputs.verified
  -> run @actions.get_account with email: @variables.email
     set @variables.account = @outputs.account_data
  -> run @actions.get_orders with account_id: @variables.account.id
     set @variables.orders = @outputs.order_list
```

### <span data-proof="authored" data-by="ai:claude">2. Fetch Data Before Reasoning</span>

<span data-proof="authored" data-by="ai:claude">Retrieve data deterministically before the LLM sees the prompt:</span>

```
reasoning:
  -> run @actions.get_customer_profile with id: @variables.customer_id
     set @variables.profile = @outputs.customer_profile
  | The customer's profile shows: {!@variables.profile}.
  | Use this information to personalize your response.
```

### <span data-proof="authored" data-by="ai:claude">3. Filtering with Available When</span>

<span data-proof="authored" data-by="ai:claude">Control tool visibility based on state:</span>

```
reasoning.actions:
  - name: apply_discount
    action: @actions.apply_discount_code
    description: Apply a promotional discount to the order
    available when: @variables.order_total > 50
```

### <span data-proof="authored" data-by="ai:claude">4. Required Topic Workflow</span>

<span data-proof="authored" data-by="ai:claude">Enforce mandatory steps before proceeding:</span>

```
topic identity_verification:
  description: Verifies customer identity before allowing access
  reasoning:
    -> if @variables.is_verified == False
      | I need to verify your identity first. Can you provide your email and order number?
    -> if @variables.is_verified == True
      -> @utils.transition to @topic.account_management
```

### <span data-proof="authored" data-by="ai:claude">5. System Overrides Per Topic</span>

<span data-proof="authored" data-by="ai:claude">Override global system instructions for a specific topic:</span>

```
topic sensitive_billing:
  description: Handles billing disputes
  system_override:
    | You are now in billing dispute mode. Be extra careful with financial information.
    | Never disclose full credit card numbers. Always mask as ****1234.
  reasoning:
    | Help the customer resolve their billing concern.
```

### <span data-proof="authored" data-by="ai:claude">6. Context Engineering</span>

<span data-proof="authored" data-by="ai:claude">Provide the LLM with rich context for better decisions:</span>

```
reasoning:
  -> run @actions.get_customer_history with id: @variables.customer_id
     set @variables.history = @outputs.history
  | Customer context:
  | - Name: {!@variables.customer_name}
  | - Account tier: {!@variables.account_tier}
  | - Previous interactions: {!@variables.history}
  | Use this context to provide informed, personalized assistance.
```

### <span data-proof="authored" data-by="ai:claude">7. Topic Selector in start_agent</span>

<span data-proof="authored" data-by="ai:claude">Configure effective routing:</span>

```
start_agent:
  description: Classifies and routes customer requests
  reasoning:
    -> set @variables.num_turns = @variables.num_turns + 1
    | Analyze the customer's message and route to the most appropriate topic.
    | Consider the conversation history and current context.
  actions:
    - @topic.order_status
    - @topic.returns_and_exchanges
    - @topic.billing
    - @topic.general_questions
```

### <span data-proof="authored" data-by="ai:claude">8. Resource References in Prompts</span>

<span data-proof="authored" data-by="ai:claude">Explicitly mention resources so the LLM knows they exist:</span>

```
reasoning:
  | If the customer asks about their order, use @actions.get_order_status to look it up.
  | If they want to return an item, transition to @topic.returns.
```

***

## <span data-proof="authored" data-by="ai:claude">Examples</span>

### <span data-proof="authored" data-by="ai:claude">Customer Support Agent</span>

```
config:
  developer_name: customer_support
  label: Customer Support Agent
  type: AgentforceServiceAgent
  version: 1.0

variables:
  customer_name: mutable string
  customer_email: mutable string
  is_verified: mutable boolean = False
  order_id: mutable string
  order_status: mutable string
  num_turns: mutable number = 0

system:
  welcome:
    | Hello! Welcome to Acme Support. How can I help you today?
  error:
    | I apologize, but I encountered an error. Let me try again.

connection:
  messaging:
    outbound_route_type: queue
    outbound_route_name: Support_Queue

start_agent:
  description: Routes customer to the appropriate support topic
  reasoning:
    -> set @variables.num_turns = @variables.num_turns + 1
    | Classify the customer's request and route appropriately.
  actions:
    - @topic.identity_verification
    - @topic.order_inquiry
    - @topic.general_help

topic identity_verification:
  description: Verifies customer identity using email and order number
  reasoning:
    -> if @variables.is_verified == True
      | The customer is already verified. Ask how you can help.
    -> else
      | Ask the customer for their email address and order number to verify their identity.
    -> @utils.set variable @variables.customer_email
       description: The email address the customer provided
       ...
    -> @utils.set variable @variables.order_id
       description: The order number the customer provided
       ...
    -> if @variables.customer_email is not None
      -> run @actions.verify_customer with email: @variables.customer_email, order_id: @variables.order_id
         set @variables.is_verified = @outputs.verified
         set @variables.customer_name = @outputs.name

topic order_inquiry:
  description: Looks up and reports order status
  reasoning:
    -> if @variables.is_verified == False
      -> @utils.transition to @topic.identity_verification
    -> run @actions.get_order_status with order_id: @variables.order_id
       set @variables.order_status = @outputs.status
    | The order {!@variables.order_id} status is: {!@variables.order_status}.
    | Provide a helpful summary to {!@variables.customer_name}.
  reasoning.actions:
    - name: escalate_to_human
      action: @utils.escalate
      description: Transfer to a human agent if the customer is unsatisfied
      available when: @variables.num_turns > 3

topic general_help:
  description: Handles general customer questions
  reasoning:
    | Help the customer with their general inquiry.
    | If they need order-specific help, suggest verifying their identity first.
```

### <span data-proof="authored" data-by="ai:claude">Multi-Turn Interview Agent</span>

```
config:
  developer_name: intake_interview
  label: Intake Interview Agent
  type: AgentforceServiceAgent
  version: 1.0

variables:
  current_step: mutable number = 1
  full_name: mutable string
  company: mutable string
  use_case: mutable string
  budget_range: mutable string
  interview_complete: mutable boolean = False

system:
  welcome:
    | Hi! I'd like to learn about your needs. I'll ask you a few questions.
  error:
    | Sorry, I hit a snag. Let me continue where we left off.

start_agent:
  description: Manages the interview flow step by step
  reasoning:
    | Continue the intake interview at the current step.
  actions:
    - @topic.interview

topic interview:
  description: Sequential interview collecting name, company, use case, and budget
  reasoning:
    # Step 1: Name
    -> if @variables.current_step == 1
      | Ask the customer for their full name.
      -> @utils.set variable @variables.full_name
         description: The customer's full name
         ...
      -> if @variables.full_name is not None
        -> set @variables.current_step = 2

    # Step 2: Company
    -> if @variables.current_step == 2
      | Great, {!@variables.full_name}! What company are you with?
      -> @utils.set variable @variables.company
         description: The company name the customer provided
         ...
      -> if @variables.company is not None
        -> set @variables.current_step = 3

    # Step 3: Use case
    -> if @variables.current_step == 3
      | What's your primary use case or challenge you're trying to solve?
      -> @utils.set variable @variables.use_case
         description: The customer's primary use case or challenge
         ...
      -> if @variables.use_case is not None
        -> set @variables.current_step = 4

    # Step 4: Budget
    -> if @variables.current_step == 4
      | Last question — what's your approximate budget range?
      -> @utils.set variable @variables.budget_range
         description: The customer's budget range
         ...
      -> if @variables.budget_range is not None
        -> set @variables.current_step = 5
        -> set @variables.interview_complete = True

    # Complete
    -> if @variables.interview_complete == True
      | Thank you, {!@variables.full_name}! Here's a summary:
      | - Name: {!@variables.full_name}
      | - Company: {!@variables.company}
      | - Use Case: {!@variables.use_case}
      | - Budget: {!@variables.budget_range}
      | A team member will follow up shortly.
```

***

## <span data-proof="authored" data-by="ai:claude">Syntax Quick Reference</span>

| <span data-proof="authored" data-by="ai:claude">Symbol</span>                                                                                                                      | <span data-proof="authored" data-by="ai:claude">Meaning</span>                  | <span data-proof="authored" data-by="ai:claude">Example</span>                                            |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| <span data-proof="authored" data-by="ai:claude">`#`</span>                                                                                                                         | <span data-proof="authored" data-by="ai:claude">Comment</span>                  | <span data-proof="authored" data-by="ai:claude">`# This is a comment`</span>                              |
| <span data-proof="authored" data-by="ai:claude">`->`</span>                                                                                                                        | <span data-proof="authored" data-by="ai:claude">Logic instruction</span>        | <span data-proof="authored" data-by="ai:claude">`-> set @variables.x = 1`</span>                          |
| <span data-proof="authored" data-by="ai:claude">`|`</span>                                                                                                                         | <span data-proof="authored" data-by="ai:claude">Prompt instruction</span>       | <span data-proof="authored" data-by="ai:claude">`| Help the customer.`</span>                             |
| <span data-proof="authored" data-by="ai:claude">`...`</span>                                                                                                                       | <span data-proof="authored" data-by="ai:claude">Slot-fill (LLM fills in)</span> | <span data-proof="authored" data-by="ai:claude">`-> @utils.set variable @variables.x ...`</span>          |
| <span data-proof="authored" data-by="ai:claude">`{!expr}`</span>                                                                                                                   | <span data-proof="authored" data-by="ai:claude">Variable interpolation</span>   | <span data-proof="authored" data-by="ai:claude">`{!@variables.name}`</span>                               |
| <span data-proof="authored" data-by="ai:claude">`@variables.x`</span>                                                                                                              | <span data-proof="authored" data-by="ai:claude">Variable reference</span>       | <span data-proof="authored" data-by="ai:claude">`@variables.customer_name`</span>                         |
| <span data-proof="authored" data-by="ai:claude">`@actions.x`</span>                                                                                                                | <span data-proof="authored" data-by="ai:claude">Action reference</span>         | <span data-proof="authored" data-by="ai:claude">`@actions.get_order`</span>                               |
| <span data-proof="authored" data-by="ai:claude">`@topic.x`</span>                                                                                                                  | <span data-proof="authored" data-by="ai:claude">Topic reference</span>          | <span data-proof="authored" data-by="ai:claude">`@topic.returns`</span>                                   |
| <span data-proof="authored" data-by="ai:claude">`@outputs.x`</span>                                                                                                                | <span data-proof="authored" data-by="ai:claude">Action output reference</span>  | <span data-proof="authored" data-by="ai:claude">`@outputs.order_status`</span>                            |
| <span data-proof="authored" data-by="ai:claude">`@system_variables.x`</span>                                                                                                       | <span data-proof="authored" data-by="ai:claude">System variable</span>          | <span data-proof="authored" data-by="ai:claude">`@system_variables.user_input`</span>                     |
| <span data-proof="authored" data-by="ai:claude">`@utils.x`</span>                                                                                                                  | <span data-proof="authored" data-by="ai:claude">Utility function</span>         | <span data-proof="authored" data-by="ai:claude">`@utils.transition to`</span>                             |
| <span data-proof="authored" data-by="ai:claude">`run ... with ... set`</span>                                                                                                      | <span data-proof="authored" data-by="ai:claude">Execute action</span>           | <span data-proof="authored" data-by="ai:claude">`-> run @actions.foo with x: 1 set y = @outputs.z`</span> |
| <span data-proof="authored" data-by="ai:claude">`if`</span> <span data-proof="authored" data-by="ai:claude">/</span> <span data-proof="authored" data-by="ai:claude">`else`</span> | <span data-proof="authored" data-by="ai:claude">Conditional</span>              | <span data-proof="authored" data-by="ai:claude">`-> if @variables.x == True`</span>                       |
| <span data-proof="authored" data-by="ai:claude">`is None`</span>                                                                                                                   | <span data-proof="authored" data-by="ai:claude">Null check</span>               | <span data-proof="authored" data-by="ai:claude">`-> if @variables.x is None`</span>                       |
| <span data-proof="authored" data-by="ai:claude">`is not None`</span>                                                                                                               | <span data-proof="authored" data-by="ai:claude">Not null check</span>           | <span data-proof="authored" data-by="ai:claude">`-> if @variables.x is not None`</span>                   |

***

## <span data-proof="authored" data-by="ai:claude">Agentforce DX Workflow</span>

<span data-proof="authored" data-by="ai:claude">Agent Script integrates with Salesforce DX for pro-code development:</span>

### <span data-proof="authored" data-by="ai:claude">Setup</span>

1. <span data-proof="authored" data-by="ai:claude">Install Salesforce CLI (`sf`)</span>
2. <span data-proof="authored" data-by="ai:claude">Install the</span> **<span data-proof="authored" data-by="ai:claude">Agentforce Vibes IDE</span>** <span data-proof="authored" data-by="ai:claude">VS Code extension</span>
3. <span data-proof="authored" data-by="ai:claude">Connect to your Salesforce org</span>

### <span data-proof="authored" data-by="ai:claude">Development Workflow</span>

```
1. Generate authoring bundle locally
   sf agentforce generate --type agent

2. Write/edit Agent Script files in VS Code

3. Push to org for testing
   sf project deploy start

4. Refine in Agentforce Builder UI (optional)

5. Pull changes back to local project
   sf project retrieve start

6. Test via CLI, VS Code, or Testing Center UI

7. Commit to version control
```

### <span data-proof="authored" data-by="ai:claude">Key Principles</span>

* **<span data-proof="authored" data-by="ai:claude">Bidirectional sync:</span>** <span data-proof="authored" data-by="ai:claude">Code locally, push to org, refine in Builder, pull back</span>

* **<span data-proof="authored" data-by="ai:claude">Source control:</span>** <span data-proof="authored" data-by="ai:claude">Agent metadata lives in Git alongside Apex/LWC</span>

* **<span data-proof="authored" data-by="ai:claude">Always re-test after publishing</span>** <span data-proof="authored" data-by="ai:claude">— agent behavior can change after deployment</span>

* **<span data-proof="authored" data-by="ai:claude">Iterate:</span>** <span data-proof="authored" data-by="ai:claude">Switch freely between Script View, Canvas View, and local VS Code</span>

***

## <span data-proof="authored" data-by="ai:claude">Tips & Gotchas</span>

1. **<span data-proof="authored" data-by="ai:claude">Keep reasoning instructions short</span>** <span data-proof="authored" data-by="ai:claude">— shorter prompts produce more accurate, reliable LLM results</span>
2. **<span data-proof="authored" data-by="ai:claude">No</span>** **<span data-proof="authored" data-by="ai:claude">`else if`</span>** <span data-proof="authored" data-by="ai:claude">— use nested</span> <span data-proof="authored" data-by="ai:claude">`if`</span> <span data-proof="authored" data-by="ai:claude">blocks or separate conditions instead</span>
3. **<span data-proof="authored" data-by="ai:claude">Transitions are one-way</span>** <span data-proof="authored" data-by="ai:claude">—</span> <span data-proof="authored" data-by="ai:claude">`@utils.transition to`</span> <span data-proof="authored" data-by="ai:claude">discards the current prompt; use</span> <span data-proof="authored" data-by="ai:claude">`@topic.x`</span> <span data-proof="authored" data-by="ai:claude">as a tool for delegation-and-return</span>
4. **<span data-proof="authored" data-by="ai:claude">`escalate`</span><span data-proof="authored" data-by="ai:claude">is reserved</span>**  <span data-proof="authored" data-by="ai:claude">— cannot be used as a topic or action name</span>
5. **<span data-proof="authored" data-by="ai:claude">Variable naming</span>** <span data-proof="authored" data-by="ai:claude">— snake_case, no trailing/consecutive underscores, max 80 chars</span>
6. **<span data-proof="authored" data-by="ai:claude">Tool visibility drives behavior</span>** <span data-proof="authored" data-by="ai:claude">— use</span> <span data-proof="authored" data-by="ai:claude">`available when`</span> <span data-proof="authored" data-by="ai:claude">to hide irrelevant tools rather than instructing the LLM to ignore them</span>
7. **<span data-proof="authored" data-by="ai:claude">Prompt assembly happens before LLM reasoning</span>** <span data-proof="authored" data-by="ai:claude">— all</span> <span data-proof="authored" data-by="ai:claude">`->`</span> <span data-proof="authored" data-by="ai:claude">logic runs first, then the assembled prompt is sent to the LLM</span>
8. **<span data-proof="authored" data-by="ai:claude">`EinsteinHyperClassifier`</span>** <span data-proof="authored" data-by="ai:claude">is faster but doesn't support images or certain utils</span>
9. **<span data-proof="authored" data-by="ai:claude">Use</span>** **<span data-proof="authored" data-by="ai:claude">`@mention`</span><span data-proof="authored" data-by="ai:claude">references</span>**  <span data-proof="authored" data-by="ai:claude">in prompt instructions to help the LLM understand what tools and topics are available</span>
10. **<span data-proof="authored" data-by="ai:claude">Test iteratively</span>** <span data-proof="authored" data-by="ai:claude">— use the Testing Center, VS Code, or CLI to validate behavior after each change</span>